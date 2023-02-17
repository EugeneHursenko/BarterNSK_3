from app import app
from flask import render_template


@app.route('/offers')
def offers_index():
    return render_template('offers/offers.html')

