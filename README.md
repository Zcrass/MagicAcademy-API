# Magic Academy API

## Usage
To run the server, please execute the following from the root directory:
### Running locally

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

### Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```


## Description

This is the API tht process request for the Magic Academy.
Have the following endpoints:

- /solicitud: (POST) Crea una nueva solicitud
- /solicitud/{id}: (DELETE) Elimina una solicitud por ID
- /solicitud/{id}: (PUT)  Actualiza la solicitud ID
- /asignaciones: (GET) Enlista las solicitudes asignadas a cada grimorio
- /solicitud/{id}/estatus: (PATCH) obtienes el estatus de la solicitud `ID`
- /solicitudes: (GET) Enlist las solicitudes existentes en la base.
