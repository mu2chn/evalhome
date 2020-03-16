from flask import request, render_template, make_response
from apps import app, mongo, wave
from apps.models import User
import json, uuid
from datetime import datetime

@app.route('/')
def index():
    name = "Hello Apartment!"
    response = make_response(render_template('index.html', name=name))
    cookie = request.cookies.get('uid', None)
    if cookie == None:
        new_cookie = str(uuid.uuid4())
        response.set_cookie('uid', value=new_cookie)
    return response


@app.route('/eval')
def evaluate():
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    user = User(lat, lng)
    scores = wave.evaluate(user.lat, user.lng)
    user.setPoint(scores)
    aggregate = getAggregate(scores)
    mongo.db.USER.insert(
        {
            "cookie": request.cookies.get('uid', None),
            "lng": lng,
            "lat": lat,
            "point": scores['total_points'],
            "date": int(datetime.now().strftime('%s'))
        }
    )
    return json.dumps({"scores":scores, "aggregate": aggregate}, default=default_method)


def default_method(item):
    if isinstance(item, object) and hasattr(item, '__dict__'):
        return item.__dict__
    else:
        raise TypeError


def getAggregate(score):
    aggregate = {}
    result = mongo.db.USER.aggregate([
        {
            "$group":{
                "_id": "",
                "avg": {"$avg": "$point"},
                "stddev": {"$stdDevPop": "$point"},
                "point": {"$first": "$point"},
                "cnt": {"$sum": 1}
            }
        }
    ])
    res = list(result)[0]
    aggregate['dev'] = int((score['total_points']-res["avg"])/res["stddev"]*10+50)

    count = res['cnt']
    upper = mongo.db.USER.find({"point": {"$gte": score['total_points']}}).count()
    aggregate['upper'] = int(100*float(upper)/float(count))

    chart = mongo.db.USER.aggregate([
        {
            "$project": {
                "range": {
                    "$concat": [
                        {"$cond": [{"$and":[{"$lt": ["$point", 0]}]}, "0", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 0 ]}, {"$lt": ["$point", 1000]}]}, "1", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 1000 ]}, {"$lt": ["$point", 2000]}]}, "2", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 2000 ]}, {"$lt": ["$point", 3000]}]}, "3", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 3000 ]}, {"$lt": ["$point", 4000]}]}, "4", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 4000 ]}, {"$lt": ["$point", 5000]}]}, "5", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 5000 ]}, {"$lt": ["$point", 6000]}]}, "6", ""]},
                        {"$cond": [{"$and":[ {"$gte":["$point", 6000 ]}, {"$lt": ["$point", 7000]}]}, "7", ""]},
                        {"$cond": [{"$and":[{"$gte": ["$point", 7000]}]}, "-1", ""]},
                    ]
                }
            }
        },
        {
            "$group": {
                "_id" : "$range",
                "range": {"$first": "$range"},
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "range": {"$toInt": "$range"},
                "count": 1
            }
        }
    ])
    aggregate['scores'] = list(chart)
    return aggregate
