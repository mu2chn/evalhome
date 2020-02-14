from flask import request, redirect, url_for, render_template, flash
from apps import app

@app.route('/')
def index():
    name = "Hello Apartment!"
    return render_template('index.html', name=name)