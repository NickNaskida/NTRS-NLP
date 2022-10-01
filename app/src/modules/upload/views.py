from flask import Blueprint, render_template


upload_blueprint = Blueprint(
    'upload',
    __name__,
    template_folder='templates/upload'
)


@upload_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    """Upload route endpoint."""

    return render_template('upload.html')
