#!/usr/bin/python3
"""Import required libraries/modules"""
from flask import Flask, render_template, request, redirect, url_for

import web_static

app = Flask(__name__)


@app.route('/web_static/')
def index():
    return render_template('index.html')


@app.route('/run-script', methods=['POST'])
def run_script():
    print('Running script...')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    