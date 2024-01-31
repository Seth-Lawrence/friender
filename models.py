from flask_sqlalchemy import SQLAlchemy



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
        nullable=True # TODO: add default image
    )

    zip_code=db.Column(
        db.String(10),
        nullable=False
    )

    friend_radius=db.Column(
        db.Integer,
        nullable=True
        validators=[]
    )






