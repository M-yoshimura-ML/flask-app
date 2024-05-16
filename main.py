from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_ckeditor import CKEditor

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
ckeditor = CKEditor()


def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost:port/db_name'
    app.config.from_object("config.DevConfig")
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    ckeditor.init_app(app)
    with app.app_context():
        db.create_all()
    return app





