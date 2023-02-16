from app import app, bcrypt, db
from datetime import datetime
from flask import flash, render_template, redirect, url_for
from flask_login import login_required
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError
from app.forms import RegisterForm
from app.models import User


@app.route('/register', methods=('GET', 'POST'))
def user_register():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            email = form.email.data
            name = form.name.data
            password = form.password.data

            newuser = User(
                name=name,
                email=email,
                created_at=datetime.now(),
                is_enabled=True,
                password=bcrypt.generate_password_hash(password),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f'Account Succesfully created', 'success')

            return redirect(url_for('security_login'))
        except InvalidRequestError:
            db.session.rollback()
            flash(f'Something went wrong!', 'danger')
        except IntegrityError:
            db.session.rollback()
            flash(f'User already exists!.', 'warning')
        except DataError:
            db.session.rollback()
            flash(f'Invalid Entry', 'warning')
        except InterfaceError:
            db.session.rollback()
            flash(f'Error connecting to the database', 'danger')
        except DatabaseError:
            db.session.rollback()
            flash(f'Error connecting to the database', 'danger')
        except BuildError:
            db.session.rollback()
            flash(f'An error occured !', 'danger')

    return render_template('user/register.html', form=form)


@app.route('/profile', methods=('GET', 'POST'))
@login_required
def user_profile():
    return render_template('user/profile.html')
