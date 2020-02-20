from flask import request, redirect, url_for, render_template, flash
from apps import app, mongo, wave
from apps.models import User
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
    user = User(lat, lng)
    scores = wave.evaluate(user.lat, user.lng)
    user.setPoint(scores)
    aggregate = {"upper": countUpper(scores)}
    return json.dumps({"scores":scores, "aggregate": aggregate}, default=default_method)


def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError

def countUpper(score):
    count = mongo.db.USER.find().count()
    upper = mongo.db.USER.find({"point": {"$gte": score['total_points']}}).count()
    print(count, upper)
    return int(100*float(upper)/float(count))