import connexion
import six

from swagger_server.models.solicitud import Solicitud 
from swagger_server.models.student import Student 
from swagger_server import util

from swagger_server.utils import magic_modules as magic
from swagger_server.utils.db_utils import DBManager, DB_NAME, TABLE_NAME 


def add_solicitud(body): 
    """Envia una solicitud de ingreso

    Envia una solicitud de ingreso

    :param body: Envia una solicitud de ingreso
    :type body: dict | bytes

    :rtype: Solicitud
    """
    body = Student.from_dict(connexion.request.get_json())
    solicitud = body.to_dict()
    solicitud["afinidad"] = magic.assing_grimorio()
    db_manager = DBManager(DB_NAME, TABLE_NAME)
    id = db_manager.add_new_solicitud(solicitud)
    if id is not None:
        response = db_manager.get_solicitud(id)
        response = {
            "message": "Successfully added student",
            "solicitud": response
        }
        return response
    
    return "Something went wrong"


def delete_student(id_, **kwargs): 
    """Borra la solicitud del estudiante ID

    Borra la solicitud del estudiante ID

    :param id: ID del estudiante
    :type id: int

    :rtype: None
    """
    db_manager = DBManager(DB_NAME, TABLE_NAME)
    message = db_manager.delete_solicitud(id_)
    response = {
        "message": message,
        "id": id_
    }

    return response


def update_solicitud(id_, body=None): 
    """Actualiza la solicitud del estudiante ID

    Actualiza la solicitud del estudiante ID

    :param id: ID del estudiante
    :type id: int
    :param body: Actualiza la solicitud del estudiante ID
    :type body: dict | bytes

    :rtype: Solicitud
    """
    body = Solicitud.from_dict(connexion.request.get_json()) 
    solicitud = body.to_dict()
    print(solicitud)
    db_manager = DBManager(DB_NAME, TABLE_NAME)
    message = db_manager.update_solicitud(id_, solicitud)
    response = db_manager.get_solicitud(id_)
    response = {
        "message": message,
        "id": id_,
        "solicitud": response
    }
    return response

