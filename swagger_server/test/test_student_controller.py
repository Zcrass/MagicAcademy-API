# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.solicitud import Solicitud  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentController(BaseTestCase):
    """StudentController integration test stubs"""

    def test_add_solicitud(self):
        """Test case for add_solicitud

        Envia una solicitud de ingreso
        """
        body = Student()
        response = self.client.open(
            '/solicitud',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_student(self):
        """Test case for delete_student

        Borra la solicitud del estudiante ID
        """
        response = self.client.open(
            '/solicitud/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_solicitud(self):
        """Test case for update_solicitud

        Actualiza la solicitud del estudiante ID
        """
        body = Student()
        response = self.client.open(
            '/solicitud/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
