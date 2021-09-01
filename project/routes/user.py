from flask import render_template
from project.routes import user_bp

@user_bp.route('/view/', methods=['GET'])
def view():
    return render_template('view_users.html')

@user_bp.route('/create/', methods=['GET'])
def create():
    pass

@user_bp.route('/update/', methods=['GET'])
def update():
    pass

@user_bp.route('/delete/', methods=['GET'])
def delete():
    pass