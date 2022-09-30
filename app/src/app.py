from flask import Flask, render_template

from src.database import db
from src.settings import Config
from src.extensions import extensions, extensions_with_db


def import_models() -> None:
    """Import models here for Flask-Migrate to work."""
    pass

def register_extensions(app: Flask) -> None:
    """Register Flask extensions."""
    for extension in extensions:
        extension.init_app(app=app)

    for extension in extensions_with_db:
        extension.init_app(app=app, db=db)


def register_blueprints(app: Flask) -> None:
    """
    Method to register list of blueprints to the app.

    :param app: Flask application
    :return: None
    """
    # To check if app contains blueprints we need to be inside the app context
    from .utils import blueprints

    if not blueprints and app.get("CHECK_FOR_BLUEPRINTS") is True:
        message = "The list of blueprints is empty. App won't have any blueprints."
        app.logger.warning(message)
    else:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)


def register_error_handlers(app: Flask) -> None:
    """Register error handlers here."""
    pass


def register_shell_context(app: Flask) -> None:
    """Register shell context here."""
    pass


def register_commands(app: Flask) -> None:
    """Register flask commands here."""
    pass


def configure_logger() -> None:
    """Configure logger here."""
    pass


def create_app() -> Flask:
    """
    Create application factory.

    :return: Flask application
    """
    configure_logger()

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_shell_context(app)
    register_commands(app)

    return app
