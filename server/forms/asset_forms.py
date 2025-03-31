from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SubmitField, ColorField
from wtforms.validators import DataRequired, ValidationError
from flask import current_app

class AssetGenerationForm(FlaskForm):
    logo = FileField(
        'Sube tu logo (PNG)',
        validators=[DataRequired(message="¡Se requiere un archivo!")]
    )
    
    app_name = StringField(
        'Nombre de la App',
        validators=[DataRequired(message="¡El nombre es requerido!")],
        default=lambda: current_app.config['APP_NAME']
    )
    
    theme_color = ColorField(
        'Color del tema (para PWA)',
        default='#4F46E5'  # Color de Bulma (indigo)
    )
    
    submit = SubmitField('Generar Assets')

    def validate_logo(self, field):
        if not allowed_file(field.data.filename):
            raise ValidationError("¡Solo se permiten archivos PNG!")

def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']