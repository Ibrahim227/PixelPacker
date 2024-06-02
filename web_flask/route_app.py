#!/usr/bin/python3
"""Import required libraries/modules"""
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/', strict_slashes=False)
def history():
    return render_template('history.html')


@app.route('/run-script', methods=['GET'])
def run_script():
    print('Running script...')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
