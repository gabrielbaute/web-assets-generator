import os
from flask import Flask
from config import current_config
from server_logging import setup_logging
from server.routes import register_blueprints
from server.extensions import register_extensions, register_context_processors
from server.handlers import register_error_handlers

def create_app(config_class=None):
    """Factory de la aplicación Flask."""
    # 1. Configuración inicial
    app = Flask(
        __name__,
        template_folder=os.path.abspath('./templates'),  # Ruta absoluta
        static_folder=os.path.abspath('./static'),
        static_url_path=''  # Opcional: sirve staticos en la raíz (/favicon.ico)
    )
    
    # 2. Carga de configuración (prioridad: parámetro > entorno > current_config)
    config_obj = config_class or os.getenv('FLASK_CONFIG_CLASS') or current_config
    app.config.from_object(config_obj)
    setup_logging(app)
    
    # 3. Validación de configuraciones
    config_obj.validate()

    # 4. Registro de blueprints y extensiones
    register_extensions(app)
    register_blueprints(app)

    # 5. Handlers de errores personalizados
    register_error_handlers(app)

    # 6. Context processors
    register_context_processors(app)

    return app