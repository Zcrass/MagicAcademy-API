# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Solicitud(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, nombre: str=None, apellido: str=None, identificacion: str=None, edad: int=None, afinidad: str=None, aceptado: bool=None):  # noqa: E501
        """Solicitud - a model defined in Swagger

        :param id: The id of this Solicitud.  # noqa: E501
        :type id: int
        :param nombre: The nombre of this Solicitud.  # noqa: E501
        :type nombre: str
        :param apellido: The apellido of this Solicitud.  # noqa: E501
        :type apellido: str
        :param identificacion: The identificacion of this Solicitud.  # noqa: E501
        :type identificacion: str
        :param edad: The edad of this Solicitud.  # noqa: E501
        :type edad: int
        :param afinidad: The afinidad of this Solicitud.  # noqa: E501
        :type afinidad: str
        :param aceptado: The aceptado of this Solicitud.  # noqa: E501
        :type aceptado: bool
        """
        self.swagger_types = {
            'id': int,
            'nombre': str,
            'apellido': str,
            'identificacion': str,
            'edad': int,
            'afinidad': str,
            'aceptado': bool
        }

        self.attribute_map = {
            'id': 'id',
            'nombre': 'nombre',
            'apellido': 'apellido',
            'identificacion': 'identificacion',
            'edad': 'edad',
            'afinidad': 'afinidad',
            'aceptado': 'aceptado'
        }
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._identificacion = identificacion
        self._edad = edad
        self._afinidad = afinidad
        self._aceptado = aceptado

    @classmethod
    def from_dict(cls, dikt) -> 'Solicitud':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Solicitud of this Solicitud.  # noqa: E501
        :rtype: Solicitud
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Solicitud.


        :return: The id of this Solicitud.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Solicitud.


        :param id: The id of this Solicitud.
        :type id: int
        """

        self._id = id

    @property
    def nombre(self) -> str:
        """Gets the nombre of this Solicitud.


        :return: The nombre of this Solicitud.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this Solicitud.


        :param nombre: The nombre of this Solicitud.
        :type nombre: str
        """

        self._nombre = nombre

    @property
    def apellido(self) -> str:
        """Gets the apellido of this Solicitud.


        :return: The apellido of this Solicitud.
        :rtype: str
        """
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str):
        """Sets the apellido of this Solicitud.


        :param apellido: The apellido of this Solicitud.
        :type apellido: str
        """

        self._apellido = apellido

    @property
    def identificacion(self) -> str:
        """Gets the identificacion of this Solicitud.


        :return: The identificacion of this Solicitud.
        :rtype: str
        """
        return self._identificacion

    @identificacion.setter
    def identificacion(self, identificacion: str):
        """Sets the identificacion of this Solicitud.


        :param identificacion: The identificacion of this Solicitud.
        :type identificacion: str
        """

        self._identificacion = identificacion

    @property
    def edad(self) -> int:
        """Gets the edad of this Solicitud.


        :return: The edad of this Solicitud.
        :rtype: int
        """
        return self._edad

    @edad.setter
    def edad(self, edad: int):
        """Sets the edad of this Solicitud.


        :param edad: The edad of this Solicitud.
        :type edad: int
        """

        self._edad = edad

    @property
    def afinidad(self) -> str:
        """Gets the afinidad of this Solicitud.


        :return: The afinidad of this Solicitud.
        :rtype: str
        """
        return self._afinidad

    @afinidad.setter
    def afinidad(self, afinidad: str):
        """Sets the afinidad of this Solicitud.


        :param afinidad: The afinidad of this Solicitud.
        :type afinidad: str
        """

        self._afinidad = afinidad

    @property
    def aceptado(self) -> bool:
        """Gets the aceptado of this Solicitud.


        :return: The aceptado of this Solicitud.
        :rtype: bool
        """
        return self._aceptado

    @aceptado.setter
    def aceptado(self, aceptado: bool):
        """Sets the aceptado of this Solicitud.


        :param aceptado: The aceptado of this Solicitud.
        :type aceptado: bool
        """

        self._aceptado = aceptado
