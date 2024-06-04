#!/usr/bin/python3
"""Import required libraries/modules"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/history/', strict_slashes=False)
def history():
    return render_template('history')


@app.route('/login/', strict_slashes=False)
def login():
    return render_template('login')


@app.route('/home/', strict_slashes=False)
def home():
    return render_template('index')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
