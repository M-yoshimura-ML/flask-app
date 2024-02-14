from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

upload_file_bp = Blueprint('upload', __name__ , template_folder='templates')


@upload_file_bp.route('/upload')
def upload():
    return render_template('upload/upload.html')


@upload_file_bp.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(f, " as file name")
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

