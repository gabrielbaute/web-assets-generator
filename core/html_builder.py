import os
from typing import List, Dict

def generate_html_template(
    favicon_path: str,
    icons_metadata: List[Dict],  # Metadata de image_processor
    manifest_path: str,
    theme_color: str = "#000000"
) -> str:
    """
    Genera un string con el HTML necesario para incluir los assets.
    
    Args:
        favicon_path (str): Ruta al favicon.ico.
        icons (List[Dict]): Lista de iconos (ej: [{"src": "icon.png", "platform": "ios"}]).
        manifest_path (str): Ruta al manifest.json.
        theme_color (str): Color del tema para meta tags.
    
    Returns:
        str: HTML formateado.
    """
    # Meta tags básicos
    html_parts = [
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f'<link rel="icon" href="{os.path.basename(favicon_path)}">',
        f'<link rel="manifest" href="{os.path.basename(manifest_path)}">',
        f'<meta name="theme-color" content="{theme_color}">'
    ]
    
    # Iconos específicos (iOS, Android, etc.)
    for icon in icons_metadata:
        if icon["platform"] == "ios":
            html_parts.append(
                f'<link rel="apple-touch-icon" href="{os.path.basename(icon["path"])}">'
            )
        elif icon["platform"] == "android":
            html_parts.append(
                f'<link rel="icon" type="{icon["type"]}" sizes="{icon["sizes"]}" href="{os.path.basename(icon["path"])}">'
            )
    
    return "\n".join(html_parts)

def save_html_template(html_content: str, output_path: str) -> None:
    """Guarda el HTML en un archivo."""
    with open(output_path, 'w') as f:
        f.write(html_content)