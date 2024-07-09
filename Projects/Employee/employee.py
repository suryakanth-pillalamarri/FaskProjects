from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=65)])
    department = StringField('Department', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Submit')
