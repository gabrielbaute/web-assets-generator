from flask import render_template, current_app

def register_error_handlers(app):
    """Registra handlers de errores personalizados."""
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404  # Mejor en carpeta 'errors'

    @app.errorhandler(413)
    def request_entity_too_large(e):
        max_size = current_app.config['MAX_CONTENT_LENGTH'] / (1024 * 1024)  # Convertir a MB
        return render_template(
            'errors/413.html',
            max_size=int(max_size)
        ), 413