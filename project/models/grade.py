from app import db

class Grade(db.Model):
    __tablename__ = 'grades'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    grade_value = db.Column(db.Integer)