from main import db
from datetime import datetime
import pytz


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100))
    slug = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now(pytz.timezone('Asia/Tokyo')))
    updated_at = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Tokyo')))
