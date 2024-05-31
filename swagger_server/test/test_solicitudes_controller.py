# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.asignacion import Asignacion  # noqa: E501
from swagger_server.models.solicitud import Solicitud  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSolicitudesController(BaseTestCase):
    """SolicitudesController integration test stubs"""

    def test_check_status_solicitud(self):
        """Test case for check_status_solicitud

        Actualiza la solicitud del estudiante ID
        """
        body = Solicitud()
        response = self.client.open(
            '/solicitud/{id}/estatus'.format(id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_asignaciones(self):
        """Test case for get_asignaciones

        Lista las asignaciones
        """
        response = self.client.open(
            '/asignaciones',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_solicitudes(self):
        """Test case for get_solicitudes

        Lista las solicitudes
        """
        response = self.client.open(
            '/solicitudes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
