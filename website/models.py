from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    author = db.Column(db.String(100))
    desc = db.Column(db.String(1000))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    listing = db.relationship('Listing')

    def get_id(self):
        return str(self.id)
