import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()


def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:port/db_name'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password!admin@localhost:3360/flask_app'
    app.config['SECRET_KEY'] = os.urandom(24)
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    return app





