# -*- coding: utf-8 -*-
""" Settings """
import os
import logging


class Config:
    """ Settings for the application """
    APPNAME = 'Jubilarse'
    SUPPORT_EMAIL = 'westonkjones@gmail.com'
    VERSION = '0.0'
    APPID = 'westonkjones-jubilarse'
    logging.basicConfig(level=logging.DEBUG)
    DEBUG = True
    STAGING = True
    PROFILE = True
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
    POSTGRES_URL = os.getenv('POSTGRES_URL', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'postgres')
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_PORT, POSTGRES_DB)


class DevelopmentConfig(Config):
    """ Dev environment config options """
    FLASK_ENV = 'development'


class TestingConfig(Config):
    """ Testing environment config options """
    FLASK_ENV = 'testing'


class ProductionConfig(Config):
    """ Prod environment config options """
    FLASK_ENV = 'production'
    DEBUG = False
    STAGING = False
    logging.basicConfig(level=logging.INFO)


def get_config(environment='default'):
    """ Gets the correct config based on the environment """
    configs = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
    }

    return configs[environment]


CONFIG = get_config(environment=os.getenv('FLASK_ENVIRONMENT', 'default'))
