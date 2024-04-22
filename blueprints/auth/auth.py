from flask import Blueprint, request, render_template, redirect, session, flash
from passlib.hash import sha256_crypt
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from main import db, login_manager
from models.users import User
from blueprints.auth.AddUserForm import AddUserForm, LoginForm

auth_bp = Blueprint('Auth', __name__, template_folder="templates")


@auth_bp.route('/')
def top():
    return redirect('/dashboard')


@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        # hashed_pw = sha256_crypt.hash(password)
        hashed_pw = generate_password_hash(password)

        user = User(username=username, email=email, password_hash=hashed_pw)

        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('auth/signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(password):
            session['email'] = email
            login_user(user)
            return redirect('/dashboard')
        else:
            flash("email or password is wrong.")
        return render_template('auth/login.html', form=form)
    else:
        if 'email' in session:
            return redirect('/dashboard')
        return render_template('auth/login.html', form=form)


@auth_bp.route('/user/add', methods=['GET', 'POST'])
@login_required
def add_user():
    form = AddUserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            # username = form.username.data
            email = request.form.get('email')
            user = User.query.filter_by(email=email).first()
            if user is None:
                password = request.form.get('password')
                hashed_pw = generate_password_hash(password)
                favorite_color = request.form.get('favorite_color')
                user = User(username=username,
                            email=email,
                            password_hash=hashed_pw,
                            favorite_color=favorite_color)
                db.session.add(user)
                db.session.commit()
            form.username.data = ''
            form.email.data = ''
            form.password.data = ''
            flash("User Added Successfully")
        return redirect('/user/add')
    else:
        username = None
        username = form.username.data
        our_users = User.query.order_by(User.created_at)
        return render_template('auth/add_user.html', form=form, username=username, our_users=our_users)


@auth_bp.route('/user/update/<int:id>', methods=['GET', 'POST'])
@login_required
def user_update(id):
    form = AddUserForm()
    name_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.username = request.form.get('username')
        name_to_update.email = request.form.get('email')
        name_to_update.favorite_color = request.form.get('favorite_color')
        try:
            db.session.commit()
            flash('User Updated Successfully')
            return render_template('auth/update.html', form=form, name_to_update=name_to_update)
        except:
            flash('Error Looks like there was a problem')
            return render_template('auth/update.html', form=form, name_to_update=name_to_update)
    else:
        return render_template('auth/update.html', form=form, name_to_update=name_to_update, id=id)


@auth_bp.route('/user/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def user_delete(id):
    form = AddUserForm()
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully")
        return render_template('auth/add_user.html', form=form, user_to_delete=user_to_delete)
    except:
        flash("Whoops! There was a problem to delete user.")
        return render_template('auth/add_user.html', form=form, user_to_delete=user_to_delete)


def get_current_user():
    if current_user.is_authenticated:
        user_id = current_user.id
        return user_id
    else:
        return None


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
