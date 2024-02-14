from flask import Blueprint, render_template, request, redirect

student_bp = Blueprint('student', __name__, template_folder='templates')


@student_bp.route('/')
def student():
    return render_template('student/student.html')


@student_bp.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('student/result.html', result=result)

