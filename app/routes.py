import os
from app import app
from flask import render_template, send_from_directory, redirect, url_for
from flask_login import login_user, logout_user
from .forms import UsernamePasswordForm
from .models import User


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login', methods=["GET", "POST"])
def login():
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()

        if user.is_correct_password(form.password.data):
            login_user(user)

            return redirect(url_for('hi'))
        else:
            return redirect(url_for('login'))

    return render_template('security/login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('index'))


@app.route('/register')
def register():
    return render_template('security/register.html')


@app.route('/hi')
def hi():
    return render_template('hi.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

