from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Email

class EducationForm(FlaskForm):
    institution = StringField('Institution', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])

class ExperienceForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    end_date = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = StringField('Description')

class UserProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    location = StringField('Location')
    address = StringField('Address')
    email = StringField('Email', validators=[DataRequired(), Email()])
    website = StringField('Website')
    # Dynamic Fields
    educations = FieldList(FormField(EducationForm), min_entries=1)
    experiences = FieldList(FormField(ExperienceForm), min_entries=1)

    submit = SubmitField('Save')
