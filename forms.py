from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from models import User


class SignupForm(Form):
    name = StringField('Name', validators=[DataRequired("Please enter your name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your "
                                                                                                     "email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=5, message="Passwords must be 5 characters or more.")])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your "
                                                                                                     "email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign in")


class StudentForm(Form):
    name = StringField('Name: ', validators=[DataRequired("You must enter your name.")])
    advisor = SelectField(coerce=int)
    submit = SubmitField('See an advisor')

