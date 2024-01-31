import os

from flask import Flask, request, jsonify
from models import db, connect_db, User, DEFAULT_IMAGE_URL

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///friender')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.get("/api/users/<int:id>")
def get_user_by_id(id):
    '''Returns all user data for one user'''
    ...

@app.post("/api/signup")
def add_user():
    '''Attempts to create user from body of provided request. Returns token
    if successful'''

    # TODO: Figure out what this error is and handle it
    body = request.json
    print(body)
    # try:
    token = User.signup(body['first_name'],
            body['last_name'],
            body['username'],
            body['password'],
            body['zip_code'],
            body['friend_radius'],
            body.get('profile_image', DEFAULT_IMAGE_URL))
    return jsonify(token=token)
    # except:
        # raise Error()
