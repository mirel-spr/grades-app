from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__, template_folder='../templates/forms', static_folder='static')
class_bp = Blueprint('class_bp', __name__, template_folder='../templates', static_folder='static')
grade_bp = Blueprint('grade_bp', __name__, template_folder='../templates', static_folder='static')
student_bp = Blueprint('student_bp', __name__, template_folder='../templates', static_folder='static')
subject_bp = Blueprint('subject_bp', __name__, template_folder='../templates', static_folder='static')
test_bp = Blueprint('test_bp', __name__, template_folder='../templates', static_folder='static')
user_bp = Blueprint('user_bp', __name__, template_folder='../templates', static_folder='static')

from project.routes import auth, classes, grade, test, student, subject, user