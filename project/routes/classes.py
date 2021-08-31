from flask import render_template
from project.routes import class_bp

@class_bp.route('/view/', methods=['GET'])
def view():
    return render_template('view_classes.html')

@class_bp.route('/create/', methods=['GET'])
def create():
    pass

@class_bp.route('/update/', methods=['GET'])
def update():
    pass

@class_bp.route('/delete/', methods=['GET'])
def delete():
    pass