from flask import Blueprint, render_template, request, flash, redirect, url_for
from models.students import Student
from main import db

sqlalchemy_bp = Blueprint('SQLAlchemy', __name__, template_folder="templates")


@sqlalchemy_bp.route('/show_all')
def show_all():
    return render_template("student/show_all.html", students=Student.query.all())


@sqlalchemy_bp.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['address']:
            flash("Please enter all the fields", 'error')
        else:
            student = Student(request.form['name'],
                               request.form['city'],
                               request.form['address'],
                               request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('SQLAlchemy.show_all'))
    return render_template('student/new.html')
