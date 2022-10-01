# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set environment variables.
"""
import os
from pathlib import Path

from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(os.path.join(BASE_DIR, '.env'))


class Config(object):
    """Config class for flask application."""

    # Flask
    ENV = env.str("FLASK_ENV", default="production")
    DEBUG = ENV == "development"
    SECRET_KEY = env.str("SECRET_KEY")
    SEND_FILE_MAX_AGE_DEFAULT = env.int("SEND_FILE_MAX_AGE_DEFAULT")
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Database
    SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Cache
    CACHE_TYPE = env.str("CACHE_TYPE")

    # Upload
    UPLOAD_FOLDER = os.path.join(BASE_DIR, env.str("UPLOAD_FOLDER", default="uploads/"))
    ALLOWED_EXTENSIONS = ('pdf',)

    # Celery
    CELERY_BROKER_URL = "redis://localhost"
    CELERY_RESULT_BACKEND = "redis://localhost"

    @staticmethod
    def get_debug_status() -> bool:
        """Get DEBUG status."""
        return Config.DEBUG

    @staticmethod
    def get_upload_path() -> str:
        """Get Upload path."""
        return Config.UPLOAD_FOLDER

    @staticmethod
    def get_allowed_file_extensions() -> tuple:
        """Get allowed file extensions."""
        return Config.ALLOWED_EXTENSIONS

    @staticmethod
    def get_celery_config() -> tuple:
        """Get Celery config."""
        return Config.CELERY_BROKER_URL, Config.CELERY_RESULT_BACKEND
