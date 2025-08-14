import os
import tempfile
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from image_extractor import extract_images_as_base64

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/extract-images', methods=['POST'])
def extract_images():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        # Save the file to a temporary directory
        temp_dir = tempfile.mkdtemp()
        temp_path = os.path.join(temp_dir, filename)
        file.save(temp_path)

        # Process the file
        try:
            image_data = extract_images_as_base64(temp_path)
            return jsonify({'images': image_data})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up the temporary directory
            for file_in_dir in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, file_in_dir))
            os.rmdir(temp_dir)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
