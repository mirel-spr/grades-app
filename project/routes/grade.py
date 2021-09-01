from flask import render_template
from project.routes import grade_bp

@grade_bp.route('/view/', methods=['GET'])
def view():
    return render_template('view_classes.html')

@grade_bp.route('/create/', methods=['GET'])
def create():
    pass

@grade_bp.route('/update/', methods=['GET'])
def update():
    pass

@grade_bp.route('/delete/', methods=['GET'])
def delete():
    pass