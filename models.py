from flask_sqlalchemy import SQLAlchemy, CheckConstraint

DEFAULT_IMAGE_URL='' #TODO: Populate this


db = SQLAlchemy()

def connect_db(app):
    '''connect to db'''

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    '''user class for friender'''

    __tablename__ = 'users'

    id= db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name=db.Column(
        db.String(15),
        nullable=False
    )

    last_name=db.Column(
        db.String(25),
        nullable=False
    )

    username=db.Column(
        db.String(25),
        nullable=False,
        unique=True
    )

    password=db.Column(
        db.Text,
        nullable=False
    )

    profile_image=db.Column(
        db.Text,
        nullable=True,
        default=DEFAULT_IMAGE_URL
    )

    zip_code=db.Column(
        db.String(10),
        nullable=False
    )

    friend_radius=db.Column(
        db.Integer,
        CheckConstraint("friend_radius>0"),
        nullable=True
    )

class UserDislikes(db.Model):
    '''Model for users that have voted no on another'''

    __tablename__ = 'disliked_users'

    # If user A dislikes user B, this is user A
    disliking_user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    )

    # If user A dislikes user B, this is user B
    disliked_user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    )

class UserLikes(db.Model):
    '''Model for users that have voted yes on another'''

    __tablename__ = 'liked_users'

    # If user A likes user B, this is user A
    liking_user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    )

    # If user A likes user B, this is user B
    liked_user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,
        nullable=False
    )

class UserInterests(db.Model):
    '''Model for user-interest combinations'''

    __tablename__ = 'user_interests'

    id=db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    interest=db.Column(
        db.String(40),
        nullable=False
    )

class UserHobbies(db.Model):
    '''Model for user-hobby combinations'''

    __tablename__ = 'user_hobbies'

    id=db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    hobby=db.Column(
        db.String(40),
        nullable=False
    )

class Messages(db.Model):
    '''Model for messages'''

    __tablename__ = 'messages'

    id=db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    sending_user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    receiving_user_id=db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    subject=db.Column(
        db.String(100),
        nullable=False
    )

    body=db.Column(
        db.Text,
        nullable=False
    )






