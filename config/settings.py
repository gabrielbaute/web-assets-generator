"""Configuración de la aplicación Flask."""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuración de la aplicación Flask."""

    # Flask server
    APP_NAME = os.getenv('APP_NAME', 'MyApp')
    PORT=os.environ.get("PORT")
    DEBUG=os.environ.get("DEBUG")
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH')) * 1024 * 1024