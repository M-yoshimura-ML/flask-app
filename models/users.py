from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from main import db
import datetime


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"Role: {self.name}"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    favorite_color = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, default=2)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, email, password_hash, favorite_color=None):
        if favorite_color is not None:
            self.username = username
            self.email = email
            self.password_hash = password_hash
            self.favorite_color = favorite_color
        else:
            self.username = username
            self.email = email
            self.password_hash = password_hash

    def __repr__(self):
        return '<Name %r>' % self.username
