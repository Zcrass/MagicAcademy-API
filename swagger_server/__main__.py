#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.utils.db_utils import initialize_db


def main():
    initialize_db()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Magic Academy'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
