from flask import request, redirect, url_for, render_template, flash
from apps import app, mongo, wave
import json

@app.route('/')
def index():
    name = "Hello Apartment!"
    # axis = mongo.db.PLACE.find()[0]
    return render_template('index.html', name=name)

@app.route('/eval')
def evaluate():
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    scores = wave.evaluate(lat, lng)
    return json.dumps(scores, default=default_method)


def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError