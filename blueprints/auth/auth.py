from flask import Blueprint, request, render_template, redirect, session
from passlib.hash import sha256_crypt
from flask_login import login_user, login_required, logout_user
from main import db, login_manager
from models.users import User


auth_bp = Blueprint('Auth', __name__, template_folder="templates")


@auth_bp.route('/')
def top():
    return redirect('/document')


@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_pw = sha256_crypt.hash(password)

        user = User(username=username, email=email, password=hashed_pw)

        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('auth/signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if sha256_crypt.verify(password, user.password):
            session['email'] = email
            login_user(user)
            return redirect('/document')
    else:
        if 'email' in session:
            return redirect('/document')
        return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('email', None)
    return redirect('/login')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')
