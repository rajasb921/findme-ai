from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)  # create a Flask app
CORS(app)  # enable CORS on the app

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db" # configure the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disable tracking modifications to database

db = SQLAlchemy(app)  # create a SQLAlchemy database instance