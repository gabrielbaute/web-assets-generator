
def register_extensions(app):
    """Registra extensiones como Flask-SQLAlchemy, Flask-Login, etc."""
    pass  # Añade aquí tus extensiones si las necesitas

def register_context_processors(app):
    """Inyecta variables globales a los templates."""
    
    @app.context_processor
    def inject_globals():
        return {
            'app_name': app.config['APP_NAME'],
            'debug_mode': app.config['DEBUG'],
            'app_version': app.config['APP_VERSION'],
        }