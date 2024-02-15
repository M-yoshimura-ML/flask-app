from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from models.post import Post
from main import db

blog_bp = Blueprint('Blog', __name__, template_folder="templates")


@blog_bp.route('/document')
@login_required
def display_document():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    posts = Post.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template("document/blog_list.html", posts=posts)


@blog_bp.route('/create_blog', methods=['POST', 'GET'])
@login_required
def display_create():
    if request.method == "POST":
        if not request.form['title'] or not request.form['content']:
            flash("Please enter all the fields", 'error')
        else:
            title = request.form.get('title')
            content = request.form.get('content')
            post = Post(title=title, body=content)
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('Blog.display_document'))
    return render_template('document/create_blog.html', posts=Post.query.all())


@blog_bp.route("/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update_blog(id):
    post = Post.query.get(id)
    if request.method == "GET":
        return render_template('document/edit_blog.html', post=post)
    if request.method == "POST":
        if not request.form['title'] or not request.form['content']:
            flash("Please enter all the fields", 'error')
        else:
            post.title = request.form.get('title')
            post.body = request.form.get('content')

            db.session.commit()

            return redirect(url_for('Blog.display_document'))


@blog_bp.route("/delete/<int:id>", methods=['GET'])
@login_required
def delete_blog(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('Blog.display_document'))
