import os

from flask import Flask, request, jsonify
from models import db, connect_db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///friender')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.get("/users/<int: id>")
def get_user_by_id(id):
    '''Returns all user data for one user'''

