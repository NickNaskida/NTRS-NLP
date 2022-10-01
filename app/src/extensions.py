# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from celery import Celery
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_static_digest import FlaskStaticDigest

from src.database import db
from src.settings import Config

CELERY_BROKER_URL, CELERY_RESULT_BACKEND = Config.get_celery_config()

migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()
celery = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

extensions = [db, cache, debug_toolbar, flask_static_digest]
extensions_with_db = [migrate]
