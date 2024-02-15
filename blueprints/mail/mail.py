from flask import Blueprint
from flask_mail import Mail, Message
from main import mail

mail_bp = Blueprint('mail', __name__, template_folder="templates")


@mail_bp.route('/mail')
def send_mail():
    msg = Message('Hello', sender='no-reply-admin@gmail.com', recipients=['your_email@gmail.com'])
    msg.body = "Hello Flask! This message is sent from Flask-Mail"
    mail.send(msg)
    return "message sent"
