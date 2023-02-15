from flask import Flask
from flask_alembic import Alembic
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            instance_relative_config=True,
            static_url_path='',
            static_folder='static',
            template_folder='templates',
            )
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)
app.config.from_prefixed_env()

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

alembic = Alembic(app)

from app import cli, models, security, routes
