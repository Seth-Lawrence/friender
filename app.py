import os

from flask import Flask, request, jsonify
from models import db, connect_db, User, DEFAULT_IMAGE_URL

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///friender')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)



#### signup / login routes


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


@app.post('/api/login')
def login():
    user_creds = request.body

    username = user_creds.username
    password = user_creds.password

    token = User.validate_login(username, password) # token or false

    return jsonify(token=token)


@app.post('/api/logout')
def logout():
    ...



### USER ROUTES

@app.get('/api/users')
def get_users():
    '''gets all users returns json of users'''
    users = User.query.all()
    return jsonify(users=users)


@app.get("/api/users/<int:id>")
def get_user_by_id(id):
    '''Returns all user data for one user'''

    user = User.query.filter(User.id==id).one_or_none()

    return jsonify(user=user)



@app.patch('/api/user/<id>/edit')
def edit_user():
    '''optionally edits user first name, last name, profile image
    zip code, and friend radius. returns updated user json'''

    user = User.query.filter(User.id==id).one_or_none()

    form = request.json

    user.first_name = form.first_name or user.first_name
    user.last_name = form.last_name or user.last_name
    user.profile_image = form.profile_image or user.profile_image
    user.zip_code = form.zip_code or user.zip_code
    user.friend_radius = form.friend_radius or user.friend_radius


    db.session.add(user)
    db.session.commit()

    return jsonify(user=user)


### LIKE ROUTES

@app.post('/api/users/<int:id>/like')
def like():
    '''likes user'''
    ...


@app.post('/api/users/<int:id>/dislike')
def dislike():
    '''dislikes user'''
    ...

