#!/usr/bin/python3
"""Import required libraries/modules"""
import io
import os

from dotenv import load_dotenv

from PIL import Image
from flask import Flask, request, send_file, make_response, url_for, redirect
from flask import render_template
from werkzeug.utils import secure_filename

# from models.user import User

load_dotenv()

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_image():
    if 'file' not in request.files or 'format' not in request.form:
        return 'No file or format provided', 400

    file = request.files['file']
    formatt = request.form['format'].upper()

    if file.filename == '':
        return 'No selected file', 400

    try:
        # Save the original file temporarily to calculate its size
        original_file_path = os.path.join('uploads', secure_filename(file.filename))
        os.makedirs('uploads', exist_ok=True)
        file.save(original_file_path)
        original_size = os.path.getsize(original_file_path)

        # Convert the image
        img = Image.open(original_file_path)
        img_io = io.BytesIO()
        img.save(img_io, formatt)
        img_io.seek(0)
        converted_size = img_io.getbuffer().nbytes

        # Prepare the response
        original_filename = file.filename
        base_filename = original_filename.rsplit('.', 1)[0]
        new_filename = f"{base_filename}.{formatt.lower()}"

        response = make_response(send_file(img_io, mimetype=f'image/{formatt.lower()}'))
        response.headers['Content-Disposition'] = f'attachment; filename={new_filename}'

        # Include file size information in the headers
        response.headers['X-Original-Size'] = str(original_size)
        response.headers['X-Converted-Size'] = str(converted_size)

        # Clean up the original file
        os.remove(original_file_path)

        return response
    except Exception as e:
        return str(e), 500


@app.route('/history/', strict_slashes=False, methods=['GET', 'POST'])
def history():
    return render_template('history.html')


@app.route('/login/', strict_slashes=False, methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/home/', strict_slashes=False, methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/register/', strict_slashes=False, methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        address = request.form['address']

        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, phone=phone,
                        address=address)
        return redirect(url_for('success'))
    return render_template('register.html')


@app.route('/success')
def success():
    return "Registration successful!"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
