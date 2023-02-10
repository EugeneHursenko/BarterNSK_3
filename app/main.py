from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/hi')
def hi():
    return render_template('hi.html')
