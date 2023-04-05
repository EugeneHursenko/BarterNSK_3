import os
basedir = os.path.abspath(os.path.dirname(__file__))

TIMEZONE='Asia/Novosibirsk'
SQLALCHEMY_DATABASE_URI = 'mysql://user:1234@127.0.0.1:3306/barter_nsk'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
SQLALCHEMY_ECHO = False
SECRET_KEY = '!!! Нужно перегрузить в instance/config.py'
