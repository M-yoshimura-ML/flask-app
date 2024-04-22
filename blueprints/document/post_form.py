from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    body = StringField("body", validators=[DataRequired()], widget=TextArea())
    author = StringField("author")
    slug = StringField("Slug")
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

