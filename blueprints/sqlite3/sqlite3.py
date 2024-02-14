from flask import Blueprint, render_template, request
import sqlite3 as sql

sqlite3_db = Blueprint('sqlite3', __name__, template_folder="templates")


@sqlite3_db.route('/home')
def home():
    return render_template("student/home.html")


@sqlite3_db.route("/register")
def new_student():
    return render_template('student/register_student.html')


@sqlite3_db.route('/add_new_student', methods=['POST', 'GET'])
def add_new_student():
    if request.method == "POST":
        try:
            name = request.form.get('name')
            address = request.form.get('address')
            city = request.form.get('city')
            pin = request.form.get('pin')
            with sql.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students(name, address, city, pin) VALUES(?,?,?,?)",
                            (name, address, city, pin))
                con.commit()
                msg = "Record added successfully"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            con.close()
            return render_template('student/success.html', msg=msg)


@sqlite3_db.route('/list')
def display_student_list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return render_template("student/list.html", rows=rows)

