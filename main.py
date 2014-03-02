import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile('config.py')

# db = MongoEngine(app)

@app.route('/')
def home():
    return "Coming Soon"
