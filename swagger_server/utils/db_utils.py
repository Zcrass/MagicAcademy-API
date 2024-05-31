import logging
import json
import os
import sqlite3

from dotenv import load_dotenv
from werkzeug.exceptions import NotFound

from swagger_server.models.solicitud import Solicitud  # noqa: E501
from swagger_server.utils.magic_modules import GRIMORIO_PROBABILITIES

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

load_dotenv()


cfg = json.load(open(os.environ["DB_CONFIG_FILE"], 'r'))["create_db"]
DB_NAME = cfg["db_name"]
TABLE_NAME = cfg["table_name"]

class DBManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
            
    @staticmethod
    def generate_creation_statemen(cfg: dict) -> str:
        fields_definition = ", ".join([f"{key} {value}" for key, value in cfg["fields"].items()])
        fields_definition = fields_definition + ", creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, last_update TIMESTAMP)"

        statement = F"CREATE TABLE IF NOT EXISTS {cfg['table_name']} (id INTEGER PRIMARY KEY AUTOINCREMENT, "    
        statement = statement + fields_definition

        logger.debug(f"statement: {statement}")
        return statement

    @staticmethod   
    def _create_empty_table(db_name: str, statemen: str) -> None:
        logger.info(f"Creating table in db {db_name}...")
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute(statemen)
            cursor.close()
            conn.close()
            logger.info(f"Successfully created table in db {db_name}")

        except sqlite3.Error as error:
            logger.error("Error while creating a sqlite table")
            raise error

        return None

    @staticmethod
    def _check_table_exists(db_name: str, table_name: str):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        )
        tables = cursor.fetchone()
        cursor.close()
        conn.close()

        if tables is None:
            logger.warning(f"Table {table_name} does not exist in database {db_name}")
            return False
        return True

    def add_new_solicitud(self, student: dict) -> int:
        logger.info(f"Adding student {student} to table {self.table_name}")
        cursor = self.conn.cursor()
        cursor.execute(
            f"""INSERT INTO {self.table_name} 
            (nombre, apellido, identificacion, edad, afinidad, aceptado) 
            VALUES 
            ('{student['nombre']}', '{student['apellido']}', '{student['identificacion']}', '{student['edad']}', '{student['afinidad']}', False)"""
        )
        self.conn.commit()
        id = cursor.lastrowid
        cursor.close()
        logger.info(f"Successfully added student {student['nombre']} to table {self.table_name}")
        if id is None:
            raise sqlite3.Error("Something went wrong when adding the student")
        return id

    def get_solicitud(self, id: int) -> Solicitud:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = {id}")
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            message = f"Student with id {id} does not exist in table {self.table_name}"
            logger.error(message)
            raise NotFound(message)
            
        solicitud = dict(zip(["id", "nombre", "apellido", "identificacion", "edad", "afinidad", "aceptado"], row))
        logger.info(f"Successfully retrieved student with id {id} from table {self.table_name}")
        logger.debug(f"Solicitud: {solicitud}")
        return Solicitud(**solicitud)

    def delete_solicitud(self, id: int) -> str:        
        self.get_solicitud(id)
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = {id}")
        self.conn.commit()
        cursor.close()
        message = f"Successfully deleted student with id {id} from table {TABLE_NAME}"
        logger.info(message)
        return message
    
    def update_solicitud(self, id: int, solicitud: dict) -> str:
        old_solicitud =self.get_solicitud(id)
        old_solicitud = old_solicitud.to_dict()
        solicitud.pop("id", None)
        for key, value in solicitud.items():
            if (key in old_solicitud) and (value is not None):
                old_solicitud[key] = value

        cursor = self.conn.cursor()
        set_clauses = ", ".join([f"{key} = '{value}'" for key, value in old_solicitud.items()])
        statement = f"UPDATE Solicitudes SET {set_clauses} WHERE id = {id}"
        logger.info(f"statement: {statement}")
        cursor.execute(statement)
        self.conn.commit()
        cursor.close()
        message = f"Successfully updated student with id {id} in table {TABLE_NAME}"
        logger.info(message)
        return message
        
    def get_all_solicitudes(self) -> list:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = cursor.fetchall()
        cursor.close()
        logger.info(f"Successfully retrieved all solicitudes from table {self.table_name}")
        return [Solicitud(**dict(zip(["id", "nombre", "apellido", "identificacion", "edad", "afinidad", "aceptado"], row))) for row in rows]

    def get_asignaciones(self) -> dict:
        asignaciones = {}
        cursor = self.conn.cursor()
        for grimorio in GRIMORIO_PROBABILITIES.keys():
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE afinidad = '{grimorio}'")
            rows = cursor.fetchall()
            rows = [dict(zip(["id", "nombre", "apellido", "identificacion", "edad", "afinidad", "aceptado"], row)) for row in rows]
            asignaciones[grimorio] = rows

        cursor.close()
        logger.info(f"Successfully retrieved all asignaciones from table {self.table_name}")
        return asignaciones


    def get_status(self, id: int) -> bool:
        solicitud = self.get_solicitud(id)
        
        return bool(solicitud.aceptado)

def initialize_db() -> None:
    """Check if a SQLite db and a table exist and if not is created"""
    cfg = json.load(open(os.environ["DB_CONFIG_FILE"], 'r'))["create_db"]
    db_name = DB_NAME
    table_name = TABLE_NAME

    if cfg["db_name"] in os.listdir():
        logger.info(f"Database {db_name} already exists")
        if DBManager._check_table_exists(db_name, table_name):
            logger.info(f"Table {cfg['table_name']} already exists")
            return None
    
    logger.info(f"Table {cfg['table_name']} does not exist in database {db_name}")
    statement = DBManager.generate_creation_statemen(cfg)
    DBManager._create_empty_table(db_name, statement)
    return None
