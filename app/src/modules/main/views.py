from flask import Blueprint, render_template, request, send_from_directory

from src.settings import Config
from src.modules.upload.models import FileModel
from src.modules.main.services import filter_files

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='templates/main'
)


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Main route endpoint."""
    files = FileModel.query.order_by(FileModel.upload_date.desc()).all()

    if request.method == "POST":
        search_query = request.form['query']
        files = filter_files(search_query)

        return render_template('index.html', files=files, search_query=search_query)

    return render_template('index.html', files=files)


@main_blueprint.route('/uploads/<path:filename>', methods=['GET'])
def download(filename):
    full_path = Config.get_upload_path()
    return send_from_directory(full_path, filename)
