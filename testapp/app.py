#!/usr/local/bin/python
from flask import Flask, render_template
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template("about.html", title="About")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
