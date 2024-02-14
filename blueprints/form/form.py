from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField, RadioField, SelectField, StringField

from wtforms import validators, ValidationError


class ContactForm(FlaskForm):
    name = StringField("Name of Student", [validators.DataRequired("Please enter your name.")])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField("Address")
    email = StringField("Email", [validators.DataRequired("Please enter your email address"),
                                  validators.Email("Please enter your proper email address ")])
    age = IntegerField("age")
    language = SelectField("Language", choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")
