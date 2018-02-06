from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'advisors'
    advisorid = db.Column(db.Integer, primary_key=True)
    advisorname = db.Column(db.VARCHAR(200))
#    faculty = db.Column(db.Boolean)
#    specialty = db.Column(db.VARCHAR(200))
    email = db.Column(db.VARCHAR(200))
    password = db.Column(db.TEXT)


    def __repr__(self):
        return self.advisorname

    def __init__(self, advisorname, email, password):
        self.advisorname = advisorname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Meeting(db.Model):
    __tablename__ = 'meetings'
    meetingid = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.TEXT)
    advisorid = db.Column(db.Integer)
    meetingtime = db.Column(db.TIMESTAMP)
#    notes = db.Column(db.TEXT)
    seenyet2 = db.Column(db.Integer)

    def __init__(self, studentname, advisor):
        self.studentname = studentname
        self.advisorid = advisor



class Student(db.Model):
    __tablename__ = 'students'
    studentid = db.Column(db.Integer, primary_key=True)
    studentname = db.Column(db.TEXT)



