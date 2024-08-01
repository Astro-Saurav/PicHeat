from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load a pre-trained model (e.g., MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

def preprocess_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    image = np.array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

def get_image_score(image_path):
    image = preprocess_image(image_path)
    predictions = model.predict(image)
    score = np.max(predictions)  # Just an example, use proper scoring if available
    return score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    if 'image1' not in request.files or 'image2' not in request.files:
        return redirect(request.url)
    
    file1 = request.files['image1']
    file2 = request.files['image2']
    
    if file1.filename == '' or file2.filename == '':
        return redirect(request.url)
    
    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)
    filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    
    file1.save(filepath1)
    file2.save(filepath2)
    
    # Generate scores
    score1 = get_image_score(filepath1)
    score2 = get_image_score(filepath2)
    
    if score1 > score2:
        winner_filename = filename1
        result = f"Photo 1 Score: {score1:.2f} - Photo 2 Score: {score2:.2f}. Photo 1 is hotter."
    else:
        winner_filename = filename2
        result = f"Photo 1 Score: {score1:.2f} - Photo 2 Score: {score2:.2f}. Photo 2 is hotter."
    
    return render_template('index.html', result=result, image1_filename=filename1, image2_filename=filename2, winner_filename=winner_filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=False,host='0.0.0.0')
