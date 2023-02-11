import os
from app import app
from flask import render_template, send_from_directory, redirect, url_for


@app.route('/favicon.ico')
def static_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

