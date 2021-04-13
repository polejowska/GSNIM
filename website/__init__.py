from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-to-be-changed'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from website import routes
