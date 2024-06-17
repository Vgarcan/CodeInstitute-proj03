from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Email

class CompanyProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    since = DateField('Established Since', format='%Y-%m-%d', validators=[DataRequired()])
    location = StringField('Location')
    address = StringField('Address')
    email = StringField('Email', validators=[DataRequired(), Email()])
    website = StringField('Website')
    created_on = DateField('Created On', format='%Y-%m-%d', validators=[DataRequired()])
    last_session = DateField('Last Session', format='%Y-%m-%d', validators=[DataRequired()])

    submit = SubmitField('Save')
