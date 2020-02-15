from flask import request, redirect, url_for, render_template, flash
from apps import app, mongo
import json

@app.route('/')
def index():
    name = "Hello Apartment!"
    # axis = mongo.db.PLACE.find()[0]
    return render_template('index.html', name=name)

@app.route('/eval')
def evaluate():
    lng = request.args.get('lng')
    lat = request.args.get('lat')
    score = sampleEvaluate()
    return json.dumps(score, default=default_method)



def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

from apps.assess import Wave, PolynomialSpotFactor
def sampleEvaluate():
    superFactor = PolynomialSpotFactor("スーパー")
    superFactor.appendData("イズミヤ", 35.041133, 135.781177, 3.0)
    superFactor.appendData("カナート", 35.041141, 135.778983)
    wave = Wave()
    wave.appendFactor(superFactor, 1.2)
    scores = wave.evaluate(35.041058, 135.782566)
    return scores