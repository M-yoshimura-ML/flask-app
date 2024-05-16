from flask import render_template

from blueprints.document.post_form import SearchForm
from blueprints.helloworld.helloworld import hello_world_bp
from blueprints.student.formdata import student_bp
from blueprints.cookies.cookies import cookies_bp
from blueprints.session.session import session_bp
from blueprints.upload.upload import upload_file_bp
from blueprints.form.send_contact import send_contact_bp
from blueprints.mail.mail import mail_bp
from blueprints.sqlite3.sqlite3 import sqlite3_db
from blueprints.sqlalchemy.sqlalchemy import sqlalchemy_bp
from blueprints.document.blog import blog_bp
from blueprints.auth.auth import auth_bp
from blueprints.searchImage.search import search_image_bp
from main import create_app

app = create_app()

app.register_blueprint(hello_world_bp)
app.register_blueprint(student_bp, url_prefix="/student")
app.register_blueprint(cookies_bp, url_prefix="/cookie")
app.register_blueprint(session_bp, url_prefix="/session")
app.register_blueprint(upload_file_bp)
app.register_blueprint(send_contact_bp)
app.register_blueprint(mail_bp)
app.register_blueprint(sqlite3_db, url_prefix="/student")
app.register_blueprint(sqlalchemy_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(search_image_bp)


@app.context_processor
def inject_search_form():
    form = SearchForm()
    return dict(form=form)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html"), 500


@app.route("/test")
def test_func():
    name = 'masa'
    posts = [
        {'title': 'test1', 'author': 'masa'},
        {'title': 'test2', 'author': 'john'}
    ]
    return render_template("test.html", name=name, posts=posts)


if __name__ == "__main__":
    app.run(debug=True, port=5001)



