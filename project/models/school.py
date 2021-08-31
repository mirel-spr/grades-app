from app import db

class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100))
    users = db.relationship('User', cascade='all, delete')
    students = db.relationship('Student', cascade='all, delete')
    classes = db.relationship('Class', cascade='all, delete')
    areas = db.relationship('Area', cascade='all, delete')
    tests = db.relationship('Test', cascade='all, delete')