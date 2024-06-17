from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired

class JobApplicationForm(FlaskForm):
    job_id = HiddenField('Job ID', validators=[DataRequired()])
    user_id = HiddenField('User ID', validators=[DataRequired()])
    submit = SubmitField('Apply')
