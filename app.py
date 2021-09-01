from flask import Flask, render_template, request
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from project.routes import *
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__, template_folder='project/templates')
    app.config.from_object('config')

    # Init Packages -------------------------------------- #
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Import Models -------------------------------------- #

    from project.models.classes import Class
    from project.models.grade import Grade
    from project.models.school import School
    from project.models.student import Student
    from project.models.subject import Area, Subject
    from project.models.test import Test
    from project.models.user import User

    # flask db migrate
    # flask db upgrade

    # Register Blueprints -------------------------------------- #

    app.register_blueprint(auth_bp, url_prefix='/auth/')
    app.register_blueprint(class_bp, url_prefix='/class/')
    app.register_blueprint(grade_bp, url_prefix='/class/')
    app.register_blueprint(student_bp, url_prefix='/student/')
    app.register_blueprint(subject_bp, url_prefix='/subject/')
    app.register_blueprint(test_bp, url_prefix='/test/')
    app.register_blueprint(user_bp, url_prefix='/user/')

    # Instantiate Routes -------------------------------------- #

    @app.route('/')
    def home():
        return render_template('pages/home.html')

    if not app.debug:
        file_handler = FileHandler('error.log')
        file_handler.setFormatter(
            Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        )
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('errors')

    return app

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#





# @app.route('/about')
# def about():
#     return render_template('pages/placeholder.about.html')


# @app.route('/login')
# def login():
#     form = LoginForm(request.form)
#     return render_template('forms/login.html', form=form)


# @app.route('/register')
# def register():
#     form = RegisterForm(request.form)
#     return render_template('forms/register.html', form=form)


# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)

# Error handlers.


# @app.errorhandler(500)
# def internal_error(error):
#     #db_session.rollback()
#     return render_template('errors/500.html'), 500


# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404



#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
print(__name__)
if __name__ == '__main__':
    app = create_app()
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
