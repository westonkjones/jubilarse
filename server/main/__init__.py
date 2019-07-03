""" Initializes Flask app and provides funtions to interface with app  """
import logging
import pkgutil
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI
from flask_marshmallow import Marshmallow
from settings import CONFIG as config

LOGGER = logging.getLogger(__name__)


def create_app(name: str, configuration):
    """ Creates the flask app """
    LOGGER.info('Creating the flask application with environemnt %s ', configuration.FLASK_ENV)
    app = FlaskAPI(name, instance_relative_config=True)
    app.config.from_object(configuration)
    LOGGER.debug('Adding CORS and exposing Authorization header')
    CORS(app, expose_headers='Authorization')

    return app


def create_database(app):
    """ Initializes the database with the application """
    LOGGER.debug('Creating database connection')
    LOGGER.debug('Database location is %s', config.SQLALCHEMY_DATABASE_URI)

    database = SQLAlchemy(app)
    return database


def marshmallow_app(app):
    """ Initializes Marshmallow """
    marshmallow = Marshmallow(app)
    return marshmallow


def import_all_modules():
    """ Imports all modules so that their __init__.py is called """
    for module in pkgutil.walk_packages(path=__path__, prefix=__name__ + '.'):
        if module.ispkg:
            __import__(module.name)


APPLICATION = create_app(__name__, config)
DATABASE = create_database(APPLICATION)
MARSHMALLOW = marshmallow_app(APPLICATION)
import_all_modules()
DATABASE.create_all()
