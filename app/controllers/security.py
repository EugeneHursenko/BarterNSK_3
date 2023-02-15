from app import app
from flask import flash, render_template, redirect, url_for
from flask_bcrypt import check_password_hash
from flask_login import login_required, login_user, logout_user
from app.forms import LoginForm
from app.models import User


@app.route('/login', methods=('GET', 'POST'))
def security_login():
    form = LoginForm()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()

            if user and check_password_hash(user.password, form.password.data):
                if not user.is_enabled:
                    flash('Аккаунт отключен', 'danger')
                    return redirect(url_for('security_login'))
                else:
                    login_user(user, remember=form.remember_me.data)
                return redirect(url_for('homepage'))
            else:
                flash('Invalid Username or password!', 'danger')
        except Exception as e:
            flash(e, 'danger')

    return render_template('security/login.html', form=form)


@app.route('/logout')
@login_required
def security_logout():
    logout_user()

    return redirect(url_for('homepage'))
