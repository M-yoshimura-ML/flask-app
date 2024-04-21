from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField, RadioField, SelectField, StringField
from wtforms import validators, ValidationError


class AddUserForm(FlaskForm):
    username = StringField("User Name", [validators.DataRequired("Please enter user name.")])
    email = StringField("Email", [validators.DataRequired("Please enter email address"),
                                  validators.Email("Please enter proper email address ")])
    password = StringField("Password", [validators.DataRequired("Please enter password")])
    favorite_color = StringField("Favorite Color")
    submit = SubmitField("Send")
