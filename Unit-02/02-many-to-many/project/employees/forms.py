from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
class EmployeeForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    years_at_company = IntegerField('Years at Company', [validators.DataRequired()])
    
class DeleteForm(FlaskForm):
    pass
