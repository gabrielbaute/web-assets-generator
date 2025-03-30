from core.image_processor import generate_favicon

# Ejemplo de uso
input_image = "test_logo.png"  # Asegúrate de tener un PNG de prueba
output_dir = "static_output"   # Carpeta donde se guardarán los archivos

result = generate_favicon(input_image, output_dir)
print("Archivos generados:", result)