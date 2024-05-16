import os


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password1"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost:port/db_name"

    UPLOADS = "/home/username/app/statistics/images/uploads"


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password1"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:password!admin@localhost:3360/flask_app"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USER = "your_email@gmail.com"  # Your Gmail address
    MAIL_PASSWORD = "your_app_password"  # Generated app password
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


