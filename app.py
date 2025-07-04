from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

# Initialize Flask app
app = Flask(__name__)

# Load your trained model
MODEL_PATH = os.path.join(os.getcwd(), 'DENSENET121_Model.joblib')
model = joblib.load(MODEL_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            img_path = os.path.join('static', 'uploads', file.filename)
            file.save(img_path)

            # Preprocess image
            img = image.load_img(img_path, target_size=(128, 128))
            x = image.img_to_array(img)
            x = x / 255.0
            x = np.expand_dims(x, axis=0)

            # Predict
            pred = model.predict(x)
            # Assuming binary classification: [prob_normal, prob_pneumonia]
            label = '🔴 Pneumonia Detected' if pred[0][0] > 0.5 else '🟢 Normal'
            prediction = {'label': label, 'confidence': float(pred[0][0])}
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    # Ensure upload folder exists
    os.makedirs(os.path.join('static', 'uploads'), exist_ok=True)
    app.run(debug=True)