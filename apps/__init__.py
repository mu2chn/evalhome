from flask import Flask, Blueprint
from flask_pymongo import PyMongo
from apps.assess import Wave

# Create flask instance
app = Flask(__name__)
app.config.from_object('apps.config.Develop')

# set blueprint
js = Blueprint("js", __name__, static_url_path='/js', static_folder='./static/js')
app.register_blueprint(js)

# create wave instance
wave = Wave()

# Database options (for MongoDB)
mongo_port = 27017
mongo_host = '0.0.0.0'
app.config['MONGO_URI'] = f"mongodb://{mongo_host}:{mongo_port}/evalhome"
mongo = PyMongo(app)

import apps.views
import apps.evaluate