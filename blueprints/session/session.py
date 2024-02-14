from flask import Blueprint, render_template, session, redirect, url_for, request

session_bp = Blueprint('session', __name__, template_folder="templates")


@session_bp.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + str(username) + '<br>' + \
               "<b><a href='/session/logout'>click here to logout</a></b>"
    return "You are not logged in <br><a href='/session/login'>click here to login</a>"


@session_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        # session['username'] = request.form['username']
        session['username'] = request.form.get('username')
        return redirect(url_for('session.index'))
    return render_template('session/session.html')


@session_bp.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('session.index'))
