from app import db

class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(100))
    taken_date = db.Column((db.DateTime))
    total_grade = db.Column(db.Integer)
    pass_grade = db.Column(db.Integer)
    grades = db.relationship('Grade', cascade='all, delete')
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))