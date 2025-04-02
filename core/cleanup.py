import os
import shutil
import atexit
from flask import current_app

def init_cleanup(upload_folder):
    """Registra la limpieza de archivos temporales al cerrar la app."""
    def cleanup():
        try:
            for item in os.listdir(upload_folder):
                item_path = os.path.join(upload_folder, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path, ignore_errors=True)
                    current_app.logger.info(f"Limpiado: {item_path}")
        except Exception as e:
            if current_app:
                current_app.logger.error(f"Error en cleanup: {str(e)}")

    atexit.register(cleanup)