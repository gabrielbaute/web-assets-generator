import os
from flask import send_file, current_app
from werkzeug.utils import secure_filename
from flask_restx import Resource, fields

from server.api import api
from server.api.api_parsers import upload_parser
from core import (
    generate_favicon,
    generate_manifest,
    create_download_zip,
    create_temp_dir,
    generate_html_template,
    cleanup_temp_dir
)

@api.route('/assets')
class AssetsResource(Resource):
    @api.expect(upload_parser)
    def post(self):
        """Endpoint para generar assets"""
        try:
            args = upload_parser.parse_args()
            uploaded_file = args['file']
            app_name = args['app_name']
            theme_color = args['theme_color']

            # Validación básica
            if not uploaded_file.filename.lower().endswith('.png'):
                api.abort(400, "Solo se permiten archivos PNG")

            # Procesamiento
            temp_dir = create_temp_dir()
            filename = secure_filename(uploaded_file.filename)
            input_path = os.path.join(temp_dir, filename)
            uploaded_file.save(input_path)

            # Generar assets
            result = generate_favicon(input_path, temp_dir)
            manifest = generate_manifest(
                app_name=app_name,
                icons_metadata=result["metadata"],
                theme_color=theme_color
            )
            html = generate_html_template(
                favicon_path="favicon.ico",
                icons_metadata=result["metadata"],
                manifest_path="manifest.json",
                theme_color=theme_color
            )

            # Crear ZIP
            zip_filename = f"{app_name}_assets.zip"
            zip_path = os.path.join(temp_dir, zip_filename)
            create_download_zip(
                files=result["files"],
                output_zip_path=zip_path,
                manifest_content=manifest,
                html_content=html
            )

            # Enviar respuesta
            return send_file(
                zip_path,
                mimetype='application/zip',
                as_attachment=True,
                download_name=zip_filename
            )

        except Exception as e:
            current_app.logger.error(f"⚠️ Error en API: {str(e)}", exc_info=True)
            if 'temp_dir' in locals():
                cleanup_temp_dir(temp_dir, delay=300)
            api.abort(500, "Error interno al procesar la solicitud")