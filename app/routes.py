from app import app
from flask import render_template, send_from_directory, redirect, url_for
from .controllers import *


@app.route('/')
def homepage():
    return "Hello, World!"


@app.route('/hi')
def hi():
    return render_template('hi.html')

