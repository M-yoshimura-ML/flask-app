from flask import Blueprint, render_template, request, flash
from blueprints.form.form import ContactForm

send_contact_bp = Blueprint('SendContact', __name__, template_folder="templates")


@send_contact_bp.route("/contact", methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if not form.validate_on_submit():
            flash('All fields are required')
            return render_template('contact/contact_form.html', form=form)
        else:
            return render_template('contact/success_form.html')
    if request.method == 'GET':
        return render_template('contact/contact_form.html', form=form)

