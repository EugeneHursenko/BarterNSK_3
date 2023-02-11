from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_login import LoginManager

app = Flask(__name__,
            instance_relative_config=True,
            static_url_path='',
            static_folder='static',
            template_folder='templates',
            )
app.config.from_object('config')
app.config.from_pyfile('config.py', silent=True)
app.config.from_prefixed_env()

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

alembic = Alembic(app)

from app import cli, models, routes

from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()
