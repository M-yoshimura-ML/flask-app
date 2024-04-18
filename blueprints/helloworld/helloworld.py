from flask import Blueprint, render_template, redirect, url_for

hello_world_bp = Blueprint("helloworld", __name__, template_folder="templates")


@hello_world_bp.route("/hello")
def hello_html():
    return render_template("hello.html")


@hello_world_bp.route('/admin')
def hello_admin():
    return 'Hello admin'


@hello_world_bp.route('/hello/<guest>')
def hello_guest(guest):
    return render_template("user/user.html", user_name=guest)


@hello_world_bp.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('helloworld.hello_admin'))
    else:
        return redirect(url_for('helloworld.hello_guest', guest=name))

