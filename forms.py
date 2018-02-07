from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import User
from models import db


class SignupForm(Form):
    name = StringField('Name', validators=[DataRequired("Please enter your name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your "
                                                                                                     "email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=5, message="Passwords must be 5 characters or more.")])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Sign in")


def choice_query():
    return db.session.query(User).all()


class StudentForm(Form):
    name = StringField('Name: ', validators=[DataRequired("You must enter your name.")])
    #SelectField('Foo', coerce=int, choices=[(row.advisorid, row.advisorname) for row in User.query.group_by(User.advisorname).all()])
    #advisor = SelectField('advisor', coerce=int, choices=[(1, 'Foo 1'), (2, 'Foo 2')])
    advisor = SelectField('Pick your advisor', coerce=int, choices=[], validators=None)
    submit = SubmitField('See an advisor')



class MeetingForm(Form):
    seenstudent = BooleanField()

