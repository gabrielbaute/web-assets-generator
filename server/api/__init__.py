from flask_restx import Api
from flask import Blueprint
from config import Config

version = Config.APP_VERSION
# Blueprint para la API
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

# Configuración de la API
api = Api(
    api_bp,
    version=version,
    title='API de OctopusIcons',
    description='Genera favicons y assets programáticamente',
    doc='/docs'  # Habilita Swagger UI en /api/v1/docs
)

# Importa los recursos (endpoints) después de crear 'api' para evitar circular imports
from . import resources