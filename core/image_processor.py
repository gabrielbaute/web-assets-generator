from PIL import Image
import os
from typing import Dict, List

# Tamaños estándar para favicons y assets (en píxeles)
DEFAULT_SIZES = {
    "favicon": [(16, 16), (32, 32), (48, 48)],
    "android": [(192, 192), (512, 512)],
    "ios": [(180, 180)],  # Ejemplo para iOS (Apple Touch Icon)
}

def generate_favicon(input_path: str, output_dir: str) -> Dict[str, List[str]]:
    """
    Procesa la imagen PNG y genera favicon.ico + assets en tamaños definidos.
    
    Args:
        input_path (str): Ruta del PNG de entrada.
        output_dir (str): Carpeta donde se guardarán los archivos.
    
    Returns:
        Dict: Rutas de los archivos generados (por categoría).
    """
    generated_files = {"favicon": [], "android": [], "ios": []}
    
    try:
        # Abrir la imagen original
        original_img = Image.open(input_path)
        
        # --- Generar favicon.ico (combinación de tamaños) ---
        favicon_path = os.path.join(output_dir, "favicon.ico")
        icon_sizes = [size for size in DEFAULT_SIZES["favicon"]]
        original_img.save(favicon_path, format="ICO", sizes=icon_sizes)
        generated_files["favicon"].append(favicon_path)
        
        # --- Generar assets para Android/iOS ---
        for platform, sizes in DEFAULT_SIZES.items():
            if platform == "favicon":
                continue  # Ya procesado
            for size in sizes:
                output_path = os.path.join(output_dir, f"{platform}_{size[0]}x{size[1]}.png")
                resized_img = original_img.resize(size, Image.LANCZOS)
                resized_img.save(output_path)
                generated_files[platform].append(output_path)
        
        return generated_files
    
    except Exception as e:
        raise RuntimeError(f"Error al procesar la imagen: {e}")