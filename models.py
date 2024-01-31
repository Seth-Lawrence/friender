from flask_sqlalchemy import SQLAlchemy, CheckConstraint

DEFAULT_IMAGE_URL='https://images.unsplash.com/photo-1509987300714-11c90a6d40e7?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' #TODO: Populate this


db = SQLAlchemy()

def connect_db(app):
    '''connect to db'''

    app.app_context().push()
    db.app = app
    db.init_app(app)


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

    likes = db.relationship(
        'User',
        secondary='liked_users',
        primaryjoin=(UserLikes.liking_user_id == id),
        secondaryjoin=(UserLikes.liked_user_id == id),
        backref='liked_by'
    )

    dislikes = db.relationship(
        'User',
        secondary='disliked_users',
        primaryjoin=(UserDislikes.disliking_user_id == id),
        secondaryjoin=(UserDislikes.disliked_user_id == id),
        backref='disliked_by'
    )

    def getFriends(self):
        likes = self.likes
        liked_by = self.liked_by

        friends = [friend for friend in likes if friend in liked_by]

        return friends




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






