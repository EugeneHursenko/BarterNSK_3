import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///var/database.db'
SQLALCHEMY_ECHO = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_migrations')
