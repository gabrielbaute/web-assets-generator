"""Configuración de la aplicación Flask."""
import os
from dotenv import load_dotenv
from typing import List
from pathlib import Path


load_dotenv()

BASE_DIR = Path(__file__).parent.parent

class Config:
    """Configuración base común a todos los entornos."""
    # Seguridad
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-insecure-change-me')
    
    # Server
    HOST = os.getenv('HOST', '127.0.0.1')
    PORT = int(os.getenv('PORT', 5001))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # App
    APP_NAME = os.getenv('APP_NAME', 'OctopusIcons')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16)) * 1024 * 1024  # 16MB default
    ALLOWED_EXTENSIONS = {'png'}
    
    # Rutas
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'temp_uploads')  # Ruta absoluta
    OUTPUT_FOLDER = os.path.join(BASE_DIR, 'static_output')
    
    # CORS (opcional)
    CORS_ALLOWED_ORIGINS: List[str] = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')

    @classmethod
    def validate(cls):
        """Valida configuraciones críticas."""
        if not os.path.isdir(cls.UPLOAD_FOLDER):
            os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)
        if cls.DEBUG and cls.SECRET_KEY.startswith('dev-key-'):
            print("✅ Debug mode con clave de desarrollo")

class ProductionConfig(Config):
    """Configuración para producción."""
    DEBUG = False
    HOST = os.getenv('HOST', '0.0.0.0')
    
    @classmethod
    def validate(cls):
        super().validate()
        if not cls.SECRET_KEY or cls.SECRET_KEY.startswith('dev-key-'):
            raise ValueError("¡SECRET_KEY insegura en producción!")

class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True