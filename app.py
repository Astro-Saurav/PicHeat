from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

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
    
    # Simulated scores for testing
    score1 = 7.5
    score2 = 8.2
    
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
