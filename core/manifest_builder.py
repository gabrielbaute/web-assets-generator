import json
import os
from typing import Dict, List

def generate_manifest(
    app_name: str,
    icons_metadata: List[Dict],  # Usa la metadata de image_processor
    background_color: str = "#ffffff",
    theme_color: str = "#000000"
) -> Dict[str, any]:
    """
    Genera un diccionario con la estructura del manifest.json.
    
    Args:
        app_name (str): Nombre de la aplicación.
        icons (List[Dict]): Lista de iconos (ej: [{"src": "icon.png", "sizes": "192x192"}]).
        background_color (str): Color de fondo de la PWA.
        theme_color (str): Color del tema.
        start_url (str): URL de inicio.
    
    Returns:
        Dict: Estructura del manifest.json.
    """

    icons_for_manifest = [
        {
            "src": os.path.basename(icon["path"]),
            "sizes": icon["sizes"],
            "type": icon["type"]
        }
        for icon in icons_metadata
        if icon["platform"] == "android"  # Solo iconos para manifest
    ]
    
    return {
        "name": app_name,
        "icons": icons_for_manifest,
        "background_color": background_color,
        "theme_color": theme_color,
        "display": "standalone"
    }

def save_manifest(manifest_data: Dict[str, any], output_path: str) -> None:
    """Guarda el manifest.json en disco."""
    with open(output_path, 'w') as f:
        json.dump(manifest_data, f, indent=2)