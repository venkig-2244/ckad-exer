#!/usr/local/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return ('<h1>Home Page</h1')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
