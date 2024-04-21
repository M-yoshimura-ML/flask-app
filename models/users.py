from flask_login import UserMixin
from main import db
import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    favorite_color = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, email, password, favorite_color):
        self.username = username
        self.email = email
        self.password = password
        self.favorite_color = favorite_color

    def __repr__(self):
        return '<Name %r>' % self.username
