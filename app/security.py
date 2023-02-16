from app import app
from flask_login import LoginManager
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'security_login'


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))
