import connexion
import six

from swagger_server.models.asignacion import Asignacion  # noqa: E501
from swagger_server.models.solicitud import Solicitud  # noqa: E501
from swagger_server import util

from swagger_server.utils.db_utils import DBManager, DB_NAME, TABLE_NAME 



def check_status_solicitud(id_, body=None):  # noqa: E501
    """Revisa el estado de una solicitud

    Revisa el estado de una solicitud # noqa: E501


    :rtype: List[Solicitud]
    """
    body = Solicitud.from_dict(connexion.request.get_json())  # noqa: E501
    db_manager = DBManager(DB_NAME, TABLE_NAME)
    status = db_manager.get_status(id_)
    response = {
        "id": id_,
        "status": status
    }
    
    return response


def get_asignaciones():  # noqa: E501
    """Lista las asignaciones

    Lista las asignaciones # noqa: E501


    :rtype: List[Solicitud]
    """
    db_manager = DBManager(DB_NAME, TABLE_NAME)
    response = db_manager.get_asignaciones()
    return response



def get_solicitudes():  # noqa: E501
    """Lista las solicitudes

    Lista las solicitudes # noqa: E501


    :rtype: List[Solicitud]
    """
    db_manager = DBManager(DB_NAME, TABLE_NAME)
    response = db_manager.get_all_solicitudes()
    return response
