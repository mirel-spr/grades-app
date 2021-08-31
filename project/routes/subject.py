from flask import render_template
from project.routes import subject_bp

@subject_bp.route('/view/', methods=['GET'])
def view():
    return render_template('view_subjects.html')

@subject_bp.route('/create/subject/', methods=['GET'])
def create_subject():
    pass

@subject_bp.route('/update/subject/', methods=['GET'])
def update_subject():
    pass

@subject_bp.route('/delete/subject/', methods=['GET'])
def delete_subject():
    pass

@subject_bp.route('/create/area/', methods=['GET'])
def create_area():
    pass

@subject_bp.route('/update/area/', methods=['GET'])
def update_area():
    pass

@subject_bp.route('/delete/area/', methods=['GET'])
def delete_area():
    pass