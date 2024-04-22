import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

from blueprints.auth.auth import get_current_user
from blueprints.document.post_form import PostForm, SearchForm
from models.post import Post
from main import db

blog_bp = Blueprint('Blog', __name__, template_folder="templates")


@blog_bp.route('/blog-list')
def get_blog_list():
    page = request.args.get('page', 1, type=int)
    per_page = 3
    posts = Post.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template("document/blog_list.html", posts=posts)


@blog_bp.route('/post/<int:id>')
def get_blog(id):
    post = Post.query.get_or_404(id)
    return render_template("document/blog.html", post=post)


@blog_bp.route('/create_blog', methods=['POST', 'GET'])
@login_required
def display_create():
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user_id = get_current_user()
            title = form.title.data
            content = form.body.data
            # author = form.author.data
            slug = form.slug.data
            post = Post(title=title, body=content, user_id=user_id, slug=slug)
            form.title.data = ''
            form.body.data = ''
            form.author.data = ''
            form.slug.data = ''
            db.session.add(post)
            db.session.commit()

            flash("Blog Post submitted successfully.")
        return render_template('document/create_blog.html', form=form)
    else:
        return render_template('document/create_blog.html', form=form)


@blog_bp.route("/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update_blog(id):
    post = Post.query.get_or_404(id)
    user_id = get_current_user()
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.slug = form.slug.data
        post.body = form.body.data
        post.updated_at = datetime.datetime.now()
        db.session.add(post)
        db.session.commit()
        flash("Post has been updated")
        return redirect(url_for('Blog.update_blog', id=post.id))
    if user_id == post.user_id:
        form.title.data = post.title
        form.author.data = post.author
        form.slug.data = post.slug
        form.body.data = post.body
        return render_template('document/edit_blog.html', id=post.id, form=form)
    else:
        flash("You are not authorized to edit post.")
        return redirect(url_for('Blog.get_blog_list'))


@blog_bp.route("/delete/<int:id>", methods=['GET'])
@login_required
def delete_blog(id):
    post = Post.query.get_or_404(id)
    user_id = get_current_user()
    if user_id == post.user_id:
        try:
            db.session.delete(post)
            db.session.commit()
            flash("Blog post was deleted")
            return redirect(url_for('Blog.get_blog_list'))
        except:
            flash("Whoops there is something wrong for deleting blog.")
            return redirect(url_for('Blog.get_blog_list'))
    else:
        flash("you are not authorized to delete post.")
        return redirect(url_for('Blog.get_blog_list'))


@blog_bp.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


@blog_bp.route("/search", methods=['POST'])
def search():
    form = SearchForm()
    posts = Post.query
    if form.validate_on_submit():
        searched = form.searched.data
        posts = posts.filter(Post.body.like('%' + searched + '%')).order_by(Post.title).all()
        return render_template("/document/search_blog.html",
                               form=form,
                               searched=searched,
                               posts=posts)

