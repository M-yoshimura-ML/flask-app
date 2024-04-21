from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class AddUserForm(FlaskForm):
    username = StringField("User Name", [DataRequired("Please enter user name.")])
    email = StringField("Email", [DataRequired("Please enter email address"),
                                  Email("Please enter proper email address ")])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     EqualTo('password2', message='password must match')])
    password2 = PasswordField("Confirmed Password", validators=[DataRequired()])
    favorite_color = StringField("Favorite Color")
    submit = SubmitField("Send")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("submit")
