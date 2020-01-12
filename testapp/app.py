#!/usr/local/bin/python
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging as logger
from forms import RegistrationForm, LoginForm

logger.basicConfig(level="DEBUG")

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f57fc334364d5462924988fd555fd60a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Vibhas123@localhost/appserver'

db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'emp_details'
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.Unicode)

posts = [
    {
        'author': 'Venkatesh G',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 01, 2020'
    },
    {
        'author': 'Vibhas V G',
        'title': 'Table Tennis',
        'content': 'All about Playing Table Tennis',
        'date_posted': 'January 08, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        redirect(url_for('home'))

    return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

@app.route('/about')
def about():
    return render_template("about.html", title="About")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
