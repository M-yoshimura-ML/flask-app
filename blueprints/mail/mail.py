from flask import Blueprint
from flask_mail import Mail, Message

mail_bp = Blueprint('mail', __name__, template_folder="templates")

