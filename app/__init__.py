from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sys
import logging

app = Flask(__name__)
app.config.from_object('config')
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

db = SQLAlchemy(app)

from app import views,models