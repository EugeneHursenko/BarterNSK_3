from app import app
from flask import render_template, send_from_directory, redirect, url_for
from app.forms import UsernamePasswordForm
from app.models import User


@app.route('/register')
def user_register():
    return render_template('user/register.html')
