import os
import zipfile
import shutil
from typing import Optional

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