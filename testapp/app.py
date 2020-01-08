#!/usr/local/bin/python
from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return ('<h1>Welcome to Kubernetes Tutorial</h1')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
