import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def dist(image1, image2):
    return np.sum((image1 - image2) ** 2) ** 0.5

def KNN(X, y, test_point, k=5):
    vals = []
    for i in range(len(X)):
        trainImage = cv2.imread(os.path.join('Train/Images', X[i]))
        coloredTrainImage = cv2.cvtColor(trainImage, cv2.COLOR_BGR2RGB)
        resizedTrainImage = cv2.resize(coloredTrainImage, (100, 100))
        distance = dist(resizedTrainImage, test_point)
        vals.append((distance, y[i]))
    vals = sorted(vals)
    vals = vals[:k]

    return vals

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        image_file = request.files['image']
        if image_file.filename == '':
            return redirect(request.url)
        if image_file:
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            trainDF = pd.read_csv('Train/train.csv')
            X = trainDF.iloc[:, 0].values
            y = trainDF.iloc[:, 1].values

            img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            coloredTestImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            resizedTestImage = cv2.resize(coloredTestImage, (100, 100))
            pred = KNN(X, y, resizedTestImage)

            prediction = max(pred)[1]
            image_url = url_for('uploaded_file', filename=filename)

            return render_template('predict.html', prediction=prediction, image_url=image_url)

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
