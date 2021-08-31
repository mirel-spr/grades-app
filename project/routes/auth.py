from flask import render_template, redirect
from project.routes import auth_bp

@auth_bp.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')

@auth_bp.route('/signup/', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth_bp.route('/password-reset/', methods=['GET'])
def reset_password():
    return render_template('reset-password.html')

@auth_bp.route('/logout/', methods=['GET'])
def logout():
    return redirect('.login')