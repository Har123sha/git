# Inside your Flask backend script (flask_app.py)

from flask import Flask, request, jsonify, render_template
from full_code import process_images  # Import the function from full_code

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML template directly from the project folder
    return render_template('front-end.html')

@app.route('/process_images', methods=['POST','GET'])
def process_images_route():
    # Access the uploaded files from the request
    uploaded_files = request.files.getlist('images')

    # Call the image processing function from full_code.py
    result_path = process_images(uploaded_files)

    # Return the relative path to the processed image
    return jsonify({'imagePath': result_path})
# Inside your Flask backend script (flask_app.py)

@app.route('/result')
def result_page():
    image_path = request.args.get('image_path', None)
    if image_path is None:
        return "Image path is missing!", 400  # Bad request
    # Directly render a template that shows the image
    return render_template('result.html', image_path=image_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)