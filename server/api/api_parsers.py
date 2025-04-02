from werkzeug.datastructures import FileStorage
from flask_restx import Resource, reqparse

# Configuración del parser para form-data
upload_parser = reqparse.RequestParser()
upload_parser.add_argument(
    'file',
    type=FileStorage,
    location='files',
    required=True,
    help='Archivo PNG requerido'
)
upload_parser.add_argument(
    'app_name',
    type=str,
    location='form',
    required=True,
    help='Nombre de la aplicación requerido'
)
upload_parser.add_argument(
    'theme_color',
    type=str,
    location='form',
    required=False,
    default='#4F46E5',
    help='Color del tema (opcional)'
)