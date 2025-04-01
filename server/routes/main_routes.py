import os
from werkzeug.utils import secure_filename
from flask import (
    Blueprint, render_template, 
    send_file, flash, redirect, url_for, 
    current_app, jsonify, send_from_directory
)

from server.forms import AssetGenerationForm
from core import (
    generate_favicon, 
    generate_manifest, 
    generate_html_template, 
    create_download_zip,
    cleanup_temp_dir,
    create_temp_dir,
)

main_bp = Blueprint('main', __name__)

# Ruta 1: Formulario (GET /)
@main_bp.route('/', methods=['GET'])
def index():
    """Muestra el formulario de subida."""
    form = AssetGenerationForm()
    return render_template('main/index.html', form=form)

# Ruta 2: Procesamiento (POST /process)
@main_bp.route('/process', methods=['POST'])
def process_image():
    """Procesa la imagen y genera assets."""
    form = AssetGenerationForm()
    
    # Validación básica (WTForms + manual)
    if not form.validate_on_submit():
        flash("❌ Por favor, corrige los errores del formulario.", "danger")
        return redirect(url_for('main.index'))
    
    try:
        # Configuración inicial
        temp_dir = create_temp_dir()

        # --- 1. Guardar archivo subido ---
        uploaded_file = form.logo.data
        filename = secure_filename(uploaded_file.filename)
        input_path = os.path.join(temp_dir, filename)
        uploaded_file.save(input_path)
        
        # --- 2. Procesar imagen ---
        result = generate_favicon(
            input_path=input_path,
            output_dir=temp_dir
        )
        
        # --- 3. Generar manifest.json ---
        manifest = generate_manifest(
            app_name=form.app_name.data,
            icons_metadata=result["metadata"],
            theme_color=form.theme_color.data
        )
        
        # --- 4. Generar HTML template ---
        html = generate_html_template(
            favicon_path="favicon.ico",
            icons_metadata=result["metadata"],
            manifest_path="manifest.json",
            theme_color=form.theme_color.data
        )
        
        # --- 5. Crear ZIP ---
        zip_filename = f"{form.app_name.data}_assets.zip"
        zip_path = os.path.join(temp_dir, zip_filename)

        os.makedirs(os.path.dirname(zip_path), exist_ok=True)
        
        create_download_zip(
            files=result["files"],
            output_zip_path=zip_path,
            manifest_content=manifest,
            html_content=html
        )
        
        # --- 6. Redirigir a results.html con datos ---
        return render_template(
            'main/results.html',
            download_url=url_for('main.download_assets', filename=zip_path),
            user_app_name=form.app_name.data,
            theme_color=form.theme_color.data
        )
        
    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        cleanup_temp_dir(temp_dir)
        flash("Error al procesar la imagen", "danger")
        return redirect(url_for('main.index'))
    
    finally:
        # Limpiar el directorio temporal después de un tiempo
        cleanup_temp_dir(temp_dir, delay=300)  # Limpiar en 5 minutos

# Ruta 3: Descarga de assets (GET /download/<filename>)
@main_bp.route('/download/<filename>', methods=['GET'])
def download_assets(filename):
    """Descarga el ZIP generado."""
    flash("Archivos generados exitosamente.", "success")
    zip_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    return send_file(
        zip_path,
        as_attachment=True,
        download_name='assets.zip',
        mimetype='application/zip'
    )

@main_bp.route('/sw.js')
def service_worker():
    response = send_from_directory('static', 'sw.js')
    response.headers['Cache-Control'] = 'no-cache'
    return response