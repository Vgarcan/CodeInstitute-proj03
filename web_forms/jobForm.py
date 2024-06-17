from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DecimalField, DateField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Email, Optional

class JobInfoForm(FlaskForm):
    textual_description = TextAreaField('Textual Description', validators=[DataRequired()])
    requirements = FieldList(StringField('Requirement', validators=[Optional()]), min_entries=1)

class JobPostingForm(FlaskForm):
    company_id = StringField('Company ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    type = SelectField('Type', choices=[('on-site', 'On-Site'), ('remote', 'Remote')], validators=[DataRequired()])
    salary = DecimalField('Salary', validators=[Optional()])
    job_info = FormField(JobInfoForm)
    published_on = DateField('Published On', format='%Y-%m-%d', validators=[DataRequired()])
    finishes_on = DateField('Finishes On', format='%Y-%m-%d', validators=[DataRequired()])

    submit = SubmitField('Post Job')
