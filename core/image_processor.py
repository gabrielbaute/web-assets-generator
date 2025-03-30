from PIL import Image
import os
from typing import Dict, List

DEFAULT_SIZES = {
    "favicon": [(16, 16), (32, 32), (48, 48)],
    "android": [(192, 192), (512, 512)],
    "ios": [(180, 180)],
}

def generate_favicon(input_path: str, output_dir: str) -> Dict[str, List[Dict]]:
    """
    Procesa la imagen PNG y genera assets, retornando metadatos estructurados.
    
    Returns:
        {
            "files": ["favicon.ico", "android_192x192.png", ...],
            "metadata": [
                {"path": "android_192x192.png", "platform": "android", "sizes": "192x192"},
                {"path": "ios_180x180.png", "platform": "ios", "sizes": "180x180"},
                ...
            ]
        }
    """
    generated_files = {"files": [], "metadata": []}
    original_img = Image.open(input_path)
    
    # --- Generar favicon.ico ---
    favicon_path = os.path.join(output_dir, "favicon.ico")
    icon_sizes = [size for size in DEFAULT_SIZES["favicon"]]
    original_img.save(favicon_path, format="ICO", sizes=icon_sizes)
    generated_files["files"].append(favicon_path)
    
    # --- Generar assets para Android/iOS ---
    for platform, sizes in DEFAULT_SIZES.items():
        if platform == "favicon":
            continue
        for width, height in sizes:
            size_str = f"{width}x{height}"
            output_path = os.path.join(output_dir, f"{platform}_{size_str}.png")
            resized_img = original_img.resize((width, height), Image.LANCZOS)
            resized_img.save(output_path)
            
            generated_files["files"].append(output_path)
            generated_files["metadata"].append({
                "path": output_path,
                "platform": platform,
                "sizes": size_str,
                "type": "image/png"
            })
    
    return generated_files