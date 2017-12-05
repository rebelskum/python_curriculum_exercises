from flask import Blueprint  # we will import much more later

# let's create the owners_blueprint to register in our __init__.py
departments_blueprint = Blueprint(
    'departments',
    __name__,
    template_folder='templates'
)
