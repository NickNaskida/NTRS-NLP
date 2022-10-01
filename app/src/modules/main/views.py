from flask import Blueprint, render_template

from src.modules.upload.models import FileModel

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='templates/main'
)


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Main route endpoint."""
    files = FileModel.load_all()

    return render_template('index.html', files=files)
