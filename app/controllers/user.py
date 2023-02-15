from app import app
from flask import render_template, send_from_directory, redirect, request, url_for
from app.forms import RegisterForm
from app.models import User


@app.route('/register')
def user_register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    return render_template('user/register.html')
