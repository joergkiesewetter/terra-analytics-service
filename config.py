import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    BASE_PATH = '/terra-data/final/'
    PATH_GENERAL = BASE_PATH + 'general'
    PATH_PAYMENTS = BASE_PATH + 'payments'
    PATH_TRANSACTIONS = BASE_PATH + 'transactions'
    PATH_USER = BASE_PATH + 'user'


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
