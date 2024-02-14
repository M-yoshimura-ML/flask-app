from main import db


class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    address = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, address, pin):
        self.name = name
        self.city = city
        self.address = address
        self.pin = pin
