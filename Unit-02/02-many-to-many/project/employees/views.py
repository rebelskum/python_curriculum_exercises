from flask import Blueprint  

employees_blueprint = Blueprint(
    'employees',
    __name__,
    template_folder='templates'
)
