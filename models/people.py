from main import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    pin = db.Column(db.String(10))
