from flask import Flask, render_template, session, request, flash, redirect, url_for
from flaskext.mysql import MySQL
from models import User, Meeting, db
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignupForm, LoginForm, StudentForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://entec:entec@localhost/advising'
db = SQLAlchemy(app)
app.secret_key = "development-key"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if 'email' in session:
        return redirect(url_for('home'))
    form = SignupForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template('register.html', form=form)
        else:
            newuser = User(form.name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            session['email'] = newuser.email
            print(session['email'])
            return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template('register.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                session['id'] = User.query.filter(User.email == session['email'])
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    session.pop('email', None)
    session.pop('id', None)
    return redirect(url_for('index'))


@app.route("/", methods=["GET", "POST"])
def index():
    form = StudentForm()
    form.advisor.choices = [(int(row.advisorid), row.advisorname) for row in User.query.group_by(User.advisorname).all()]
    if request.method == "GET":
        return render_template('index.html', studentForm=form)
    else:
        return "WHAT HAPPENED?"


@app.route("/addstudent", methods=["GET", "POST"])
def addstudent():
    form = StudentForm()
    form.advisor.choices = [(int(row.advisorid), row.advisorname) for row in User.query.group_by(User.advisorname).all()]
    if request.method == "POST":
        if form.validate() == False:
            print("ERROR ADVISOR " + str(form.advisor.data))
            print("ERROR NAME " + form.name.data)
            return render_template("index.html", studentForm=form)
        else:
            newstudent = form.name.data
            advisor = int(form.advisor.data)
            print(newstudent + " is the newstudent")
            meeting = Meeting(newstudent, advisor)
            db.session.add(meeting)
            db.session.commit()
            return render_template('madeit.html', newstudent=newstudent)


@app.route("/home")
def home():
    print(session['email'] + " this is the email.")
    curemail = session['email']
    userid = User.query.filter(User.email == curemail)
    print(str(userid) + " is the userid")
    kwargs = {'email': curemail}
    number = User.query.filter_by(**kwargs)
    print(str(number.count()) + " is number")
    if number.count() is not 0:
        meetings = Meeting.query.filter(Meeting.advisorid == userid[0].advisorid)
        return render_template('advisorinfo.html', meetings=meetings, curemail=curemail, number=number)
    else:
        return render_template('advisorinfo.html', meetings=None, curemail=curemail, number=number)


if __name__ == '__main__':
    app.run(debug=True)

