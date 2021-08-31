from flask import render_template
from project.routes import test_bp

@test_bp.route('/view/', methods=['GET'])
def view():
    return render_template('view_classes.html')

@test_bp.route('/create/', methods=['GET'])
def create():
    pass

@test_bp.route('/update/', methods=['GET'])
def update():
    pass

@test_bp.route('/delete/', methods=['GET'])
def delete():
    pass