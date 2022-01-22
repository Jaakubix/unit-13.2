from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    is_done = BooleanField('is it done?', false_values=(False, 'false', 0, '0'))