from flask import render_template
from project.routes import student_bp

@student_bp.route('/view/', methods=['GET'])
def view():
    return render_template('view_students.html')

@student_bp.route('/create/', methods=['GET'])
def create():
    pass

@student_bp.route('/update/', methods=['GET'])
def update():
    # grades, student info etc
    pass

@student_bp.route('/delete/', methods=['GET'])
def delete():
    pass