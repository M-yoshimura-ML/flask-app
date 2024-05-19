from main import db, create_app
from models.users import Role

app = create_app()


with app.app_context():
    # db.create_all()
    if not Role.query.filter_by(name='admin').first():
        admin_role = Role(name='admin')
        db.session.add(admin_role)
    if not Role.query.filter_by(name='user').first():
        user_role = Role(name='user')
        db.session.add(user_role)
    db.session.commit()
