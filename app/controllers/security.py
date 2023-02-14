import os
from app import app
from flask import render_template, send_from_directory, redirect, request, url_for
from flask_login import login_user, logout_user
from app.forms import UsernamePasswordForm
from app.models import User


@app.route('/login', methods=["GET", "POST"])
def security_login():
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()

        if user.is_correct_password(form.password.data):
            login_user(user)

            return redirect(url_for('hi'))
        else:
            return redirect(url_for('security_login'))

    return render_template('security/login.html', form=form)


@app.route('/logout')
def security_logout():
    logout_user()

    return redirect(url_for('homepage'))
