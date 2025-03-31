from os import getenv
from .settings import Config, ProductionConfig, DevelopmentConfig

# Exporta todas las configuraciones relevantes
__all__ = ['Config', 'ProductionConfig', 'DevelopmentConfig']

# Opcional: Añade una variable para auto-seleccionar el entorno (útil para Flask)
current_env = getenv('FLASK_ENV', 'development')
current_config = DevelopmentConfig if current_env == 'development' else ProductionConfig