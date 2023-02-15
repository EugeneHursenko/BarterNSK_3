from app import app
from flask import render_template, session, send_from_directory, redirect, url_for
from datetime import timedelta
from .controllers import *


@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/hi')
def hi():
    return render_template('hi.html')

