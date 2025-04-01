from server import create_app
from waitress import serve
import os

app = create_app()

if __name__ == '__main__':
    if os.getenv('FLASK_ENV') == 'production':
        # Configuración para producción con Waitress
        print(f"🚀 Servidor Waitress iniciado en {app.config['HOST']}:{app.config['PORT']}")
        serve(
            app,
            host=app.config['HOST'],
            port=app.config['PORT'],
            threads=4  # Opcional: ajusta según tus necesidades
        )
    else:
        # Configuración para desarrollo
        app.run(
            host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG']
        )