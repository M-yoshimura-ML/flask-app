from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    # body = StringField("body", validators=[DataRequired()], widget=TextArea())
    body = CKEditorField('body', validators=[DataRequired()])
    author = StringField("author")
    slug = StringField("Slug")
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

