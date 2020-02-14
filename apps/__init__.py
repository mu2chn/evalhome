from flask import Flask

app = Flask(__name__)
app.config.from_object('apps.config')

import apps.views