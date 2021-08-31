from datetime import datetime
from app import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20))
    first_name = db.Column(db.String(20))
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    is_archived = db.Column(db.Boolean, default=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))


# class StudentArchive(db.Model):
#     __tablename__ = 'student_archives'

#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, unique=True)
#     last_name = db.Column(db.String(20))
#     first_name = db.Column(db.String(20))
#     created_date = db.Column(db.DateTime, default=datetime.utcnow())
#     school_id = db.Column(db.Integer, db.ForeignKey(School.id))