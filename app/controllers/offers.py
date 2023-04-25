from app import app
from flask import render_template
from flask_login import login_required, login_user, logout_user


@app.route('/offers')
def offers_index():
    return render_template('offers/offers.html')


@app.route('/offers/create')
@login_required
def offers_create():
    return render_template('offers/create.html')

