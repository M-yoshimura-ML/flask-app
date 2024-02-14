from flask import render_template, Blueprint, request, make_response

cookies_bp = Blueprint("cookies", __name__, template_folder="templates")

@cookies_bp.route("/")
def index():
    return render_template("cookie/setcookies.html")

@cookies_bp.route("/setcookie", methods=['POST', 'GET'])
def setcookies():
    if request.method == "POST":
        user = request.form['nm']
        response = make_response(render_template('cookie/readcookie.html'))
        response.set_cookie('userID', user)
        return response

@cookies_bp.route("/getcookie")
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome' + name + '</h1>'