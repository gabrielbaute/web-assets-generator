import os
import json
import zipfile
import shutil
import threading
import time
from typing import Optional, List, Dict
from flask import current_app

def create_temp_dir() -> str:
    """Crea una carpeta temporal única dentro de UPLOAD_FOLDER."""
    try:
        temp_dir = os.path.join(
            current_app.config['UPLOAD_FOLDER'], 
            f"process_{os.urandom(4).hex()}"
        )
        os.makedirs(temp_dir, exist_ok=True)
        return temp_dir
    except Exception as e:
        current_app.logger.error(f"⚠️ Error al crear el directorio temporal: {e}")
        return ""

def cleanup_temp_dir(dir_path: str, delay: int = 0) -> None:
    """Elimina un directorio temporal después de un retardo opcional (en segundos)."""
    def _delete_after_delay():
        time.sleep(delay)
        try:
            shutil.rmtree(dir_path, ignore_errors=True)
        except Exception as e:
            current_app.logger.error(f"⚠️ Error al limpiar {dir_path}: {e}")

    if delay > 0:
        thread = threading.Thread(target=_delete_after_delay)
        thread.start()
    else:
        shutil.rmtree(dir_path, ignore_errors=True)

def create_zip(files: list, output_zip: str) -> str:
    """Crea un ZIP con los archivos generados."""
    try:
        with zipfile.ZipFile(output_zip, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))
        return output_zip
    except Exception as e:
        current_app.logger.error(f"⚠️ Error al crear el ZIP: {e}")
        return ""

def create_download_zip(
    files: List[str],
    output_zip_path: str,
    manifest_content: Dict[str, any],
    html_content: str
) -> str:
    """
    Crea un ZIP con todos los assets + archivos de configuración.
    
    Args:
        files: Lista de rutas de archivos generados (ej: ["favicon.ico", "android_192x192.png"]).
        output_zip_path: Ruta donde se guardará el ZIP.
        manifest_content: Contenido del manifest.json (dict).
        html_content: Contenido del HTML (str).
    """
    try:
        with zipfile.ZipFile(output_zip_path, 'w') as zipf:
            # Añadir archivos generados
            for file_path in files:
                zipf.write(file_path, os.path.basename(file_path))
            
            # Añadir manifest.json (generado en memoria)
            zipf.writestr("manifest.json", json.dumps(manifest_content, indent=2))
            
            # Añadir template.html
            zipf.writestr("assets_template.html", html_content)
        
        return output_zip_path
    except Exception as e:
        current_app.logger.error(f"⚠️ Error al crear el ZIP: {e}")
        return ""