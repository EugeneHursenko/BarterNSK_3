import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///var/database.db'
SQLALCHEMY_ECHO = True
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_migrations')
