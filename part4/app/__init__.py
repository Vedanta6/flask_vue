from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# set up MongoDB
db = MongoEngine()
db.init_app(app)


from app import routes
from app.manager import *
