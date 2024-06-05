#!/usr/bin/python3
"""Import required libraries/modules"""
import io
import zipfile

from PIL import Image
from flask import Flask, request, send_file, make_response
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template('index5.html')


@app.route('/convert', methods=['POST'])
def convert_image():
    if 'file' not in request.files or 'format' not in request.form:
        return 'No file or format provided', 400

    files = request.files['file']
    formatt = request.form['format'].upper()

    output_files = []

    try:
        for file in files:
            if file.filename == '':
                continue

            img = Image.open(files)
            img_io = io.BytesIO()
            img.save(img_io, formatt)
            img_io.seek(0)

            original_filename = files.filename
            base_filename = original_filename.rsplit('.', 1)[0]
            new_filename = f"{base_filename}.{formatt.lower()}"

            output_files.append((new_filename, img_io))
            # Create a ZIP file if there are multiple files
        if len(output_files) > 1:
            zip_io = io.BytesIO()
            with zipfile.ZipFile(zip_io, 'w') as zip_file:
                for filename, img_io in output_files:
                    zip_file.writestr(filename, img_io.getvalue())
            zip_io.seek(0)
            return send_file(zip_io, mimetype='application/zip', as_attachment=True,
                             download_name='converted_images.zip')
        elif len(output_files) == 1:
            new_filename, img_io = output_files[0]
            response = make_response(send_file(img_io, mimetype=f'image/{formatt.lower()}'))
            response.headers['Content-Disposition'] = f'attachment; filename={new_filename}'
            return response
    except Exception as e:
        return str(e), 500


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
    app.run(debug=True, host='localhost', port=5000)
