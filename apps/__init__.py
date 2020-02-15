from flask import Flask
from flask_pymongo import PyMongo

# Create flask instance
app = Flask(__name__)
app.config.from_object('apps.config.Develop')

# Database options (for MongoDB)
mongo_port = 27017
mongo_host = '0.0.0.0'
app.config['MONGO_URI'] = f"mongodb://{mongo_host}:{mongo_port}/evalhome"
mongo = PyMongo(app)

import apps.views

import apps.test.test