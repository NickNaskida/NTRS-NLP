from flask import Blueprint, render_template, flash, redirect, url_for

from src.modules.upload.services import process_uploaded_file
from src.modules.upload.forms import FileForm

upload_blueprint = Blueprint(
    'upload',
    __name__,
    template_folder='templates/upload'
)


@upload_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    """Upload route endpoint."""
    form = FileForm()

    if form.validate_on_submit():
        process_uploaded_file(form.pdf_file.data, form.pdf_file.data.filename)

        flash('File processed successfully', 'success')
        return redirect(url_for('main.index'))

    return render_template('upload.html', form=form)
