from app import db

class Area(db.Model):
    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(60))
    colour_hex = db.Column(db.String(10))
    subjects = db.relationship('Subject', cascade='all, delete')
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(60))
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    tests = db.relationship('Test', cascade='all, delete')