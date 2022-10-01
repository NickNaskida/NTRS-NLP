from flask_wtf import FlaskForm

from flask_wtf.file import FileField, FileAllowed, FileRequired

from src.settings import Config

ALLOWED_EXTENSIONS = Config.get_allowed_file_extensions()


class FileForm(FlaskForm):
    pdf_file = FileField(validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS, 'PDF files only.')])
