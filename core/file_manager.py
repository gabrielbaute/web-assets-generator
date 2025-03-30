import os
import json
import zipfile
import shutil
from typing import Optional, List, Dict

def create_temp_dir(base_path: str = "temp") -> str:
    """Crea una carpeta temporal única."""
    temp_dir = os.path.join(base_path, os.urandom(8).hex())
    os.makedirs(temp_dir, exist_ok=True)
    return temp_dir

def cleanup_temp_dir(dir_path: str):
    """Elimina una carpeta temporal y su contenido."""
    shutil.rmtree(dir_path, ignore_errors=True)

def create_zip(files: list, output_zip: str) -> str:
    """Crea un ZIP con los archivos generados."""
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    return output_zip

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
    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        # Añadir archivos generados
        for file_path in files:
            zipf.write(file_path, os.path.basename(file_path))
        
        # Añadir manifest.json (generado en memoria)
        zipf.writestr("manifest.json", json.dumps(manifest_content, indent=2))
        
        # Añadir template.html
        zipf.writestr("assets_template.html", html_content)
    
    return output_zip_path