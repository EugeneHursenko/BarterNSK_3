from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///var/database.db"
app.config.from_object('config')
# app.register_blueprint(my_controllers)
# initialize the app with the extension
db.init_app(app)

# from app.models import *
# from app.controllers import *

from app import cli, models, routes

from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()

