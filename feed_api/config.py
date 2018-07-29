# -*- coding: utf-8 -*-

import os

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')


class BaseConfig(object):

    PROJECT = "smart_crawler"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    ADMINS = ['youremail@yourdomain.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')


class DefaultConfig(BaseConfig):

    DEBUG = True

    user = os.environ['POSTGRES_USER']
    pwd = os.environ['POSTGRES_PASSWORD']
    db = os.environ['POSTGRES_DATABASE']
    host = 'database'
    port = '5432'

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = False
    # QLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be
    # disabled by default in the future.
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLITE for prototyping.
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'
    # MYSQL for production.
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'