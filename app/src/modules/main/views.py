from flask import Blueprint, render_template


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='templates/main'
)


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Main route endpoint."""

    return render_template('index.html')
