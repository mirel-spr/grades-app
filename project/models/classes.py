from sqlalchemy.orm import backref
from app import db

class_student_xref = db.Table('class_student', db.Model.metadata,
    db.Column('class_id', db.Integer, db.ForeignKey('classes.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')))

class Class(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))
    colour_hex = db.Column(db.String(10))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    students = db.relationship('Student', secondary=class_student_xref, lazy='subquery', backref=db.backref('students', lazy=True))


# class ClassArchive(db.Model):
#     __tablename__ = 'class_archives'

#     id = db.Column(db.Integer, primary_key=True)
#     class_id = db.Column(db.Integer, unique=True)
#     class_name = db.Column(db.String(50))
#     colour_hex = db.Column(db.String(10))
#     school_id = db.Column(db.Integer, db.ForeignKey(School.id))
#     students = db.relationship('Student', secondary=class_student_xref)
