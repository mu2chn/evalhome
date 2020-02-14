from flask import request, redirect, url_for, render_template, flash
from apps import app, mongo

@app.route('/')
def index():
    name = "Hello Apartment!"
    axis = mongo.db.PLACE.find()[0]
    return render_template('index.html', name=name, axis=axis)