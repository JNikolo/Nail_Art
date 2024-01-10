from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    user_type = db.Column(db.String(15), default='cliente')
    appointments = db.relationship('Appointment')
    
