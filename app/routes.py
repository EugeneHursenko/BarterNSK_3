import os
from app import app
from flask import render_template
from flask import send_from_directory


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login')
def login():
    return render_template('security/login.html')


@app.route('/hi')
def hi():
    return render_template('hi.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

