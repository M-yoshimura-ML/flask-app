from flask import Blueprint, render_template, redirect, request, url_for, flash

login_bp = Blueprint('login', __name__, template_folder="templates")


@login_bp.route('/')
def index():
    return render_template('hello.html')


@login_bp.route('/success')
def success():
    return render_template('login/messages/flashing.html')


@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form.get('username')
        password = request.form.get('password')
        print("username:", user, ", password:", password)
        if user != 'admin' or password != 'admin':
            error = 'Invalid username or password. please try again'
        else:
            flash('You were successfully logged in')
            flash('log out before login again')
            # return redirect(url_for('login.welcome', name=user))
            return redirect(url_for('login.success'))

    return render_template('login.html', error=error)


@login_bp.route('/welcome/<name>')
def welcome(name):
    return 'welcome %s' % name



