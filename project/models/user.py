from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True, index=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(60))
    is_active = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    active_date = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    role_id = db.Column(db.Integer)