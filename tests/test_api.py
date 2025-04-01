import requests
import os
from pathlib import Path

# Configuración
API_URL = "http://localhost:5001/api/v1/assets"
TEST_IMAGE = Path("test_logo.png")  # Ruta a tu archivo PNG
APP_NAME = "MiApp"
THEME_COLOR = "#4F46E5"

def test_api():
    try:
        # 1. Verificar que el archivo existe
        if not TEST_IMAGE.exists():
            raise FileNotFoundError(f"¡El archivo {TEST_IMAGE} no existe!")

        # 2. Preparar los datos
        files = {
            'file': (TEST_IMAGE.name, open(TEST_IMAGE, 'rb')),  # (nombre, contenido)
        }
        data = {
            'app_name': APP_NAME,
            'theme_color': THEME_COLOR
        }

        print(f"🚀 Enviando {TEST_IMAGE} a la API...")

        # 3. Hacer la petición
        response = requests.post(
            API_URL,
            files=files,
            data=data,
            timeout=30  # Segundos de espera
        )

        # 4. Manejar la respuesta
        if response.status_code == 200:
            output_file = "assets_generated.zip"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            print(f"✅ ¡Éxito! ZIP guardado como {output_file}")
            print(f"Tamaño del archivo: {os.path.getsize(output_file)} bytes")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"🔥 Error inesperado: {str(e)}")

if __name__ == "__main__":
    test_api()