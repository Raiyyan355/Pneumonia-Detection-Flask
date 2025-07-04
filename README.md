
# Pneumonia Detection using Deep Learning and Flask

![Pneumonia Detection](https://img.shields.io/badge/Status-Completed-brightgreen)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

This project is a **Pneumonia Detection Web Application** that leverages **Deep Learning (DenseNet121)** to classify chest X-ray images as either **Normal** or **Pneumonia**. The solution is deployed as a lightweight web app using **Flask**.

Pneumonia is a serious lung infection that can be life-threatening if not diagnosed and treated early. This project aims to provide an easy-to-use diagnostic aid for healthcare professionals and individuals.

---

## 🚀 Features

- Upload chest X-ray images directly via the web interface.
- Real-time predictions using a pre-trained **DenseNet121** model.
- Displays prediction label (Normal/Pneumonia) along with confidence score.
- User-friendly and responsive interface.
- Secure image upload handling.

---

## 🖥️ Live Demo

*(Optional: Add the link if you deploy this project using Heroku, Render, or any other platform)*

---

## 🧩 Tech Stack

- **Frontend:** HTML, CSS (with optional Bootstrap/Tailwind)
- **Backend:** Python, Flask
- **Model:** TensorFlow, Keras, DenseNet121
- **Deployment:** (Optional: mention Heroku, AWS, etc.)
- **Others:** Joblib, NumPy

---

## 📂 Project Structure

```
Pneumonia-Detection-Flask/
│
├── static/
│   └── uploads/              # Uploaded X-ray images
│
├── templates/
│   └── index.html            # Main frontend template
│
├── DENSENET121_Model.joblib  # Pre-trained DenseNet121 model
├── app.py                    # Flask application
└── README.md                 # Project documentation
```

---

## ⚙️ How It Works

1. User uploads a chest X-ray image through the web interface.
2. The image is preprocessed (resized to 128x128, normalized).
3. The processed image is passed through a **DenseNet121** model trained for binary classification:
   - **🟢 Normal**
   - **🔴 Pneumonia Detected**
4. The result and confidence score are displayed to the user.

---

## 🔧 Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Raiyyan355/Pneumonia-Detection-Flask.git
cd Pneumonia-Detection-Flask
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note:** Make sure you have **TensorFlow**, **Flask**, **Joblib**, and other required packages installed.

### 4️⃣ Add the Pre-trained Model
Place your `DENSENET121_Model.joblib` file in the root folder.

### 5️⃣ Run the Application
```bash
python app.py
```

The app will be running at:  
`http://127.0.0.1:5000/`

---

## 📝 Sample Usage

1. Open the web browser and navigate to the app URL.
2. Upload any chest X-ray image (`.jpg`, `.png`).
3. The app will predict and show:
   ```
   🟢 Normal
   or
   🔴 Pneumonia Detected
   Confidence: 0.85 (for example)
   ```

---

## 🏆 Model Details

- **Architecture:** DenseNet121
- **Input Size:** 128x128x3
- **Output:** Binary Classification (Normal vs Pneumonia)
- **Training Dataset:** (Optional: Add dataset name if available e.g., Kaggle's Chest X-Ray Images (Pneumonia))
- **Evaluation Metrics:** Accuracy, Sensitivity, Specificity (optional to include here if available)

---

## 📊 Future Improvements

- Add visualization for Grad-CAM or heatmaps to explain predictions.
- Deploy the app online for broader accessibility.
- Enhance UI/UX using modern frontend frameworks.
- Train the model on larger and more diverse datasets.

---

## 🔒 Disclaimer

- This tool is designed for **educational** and **demonstration purposes only**.
- It should **not be used for real-world medical diagnosis** without validation by qualified healthcare professionals.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Flask](https://flask.palletsprojects.com/)
- [Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) *(Optional if used)*

---

## 🤝 Connect with Me

- **GitHub:** [Raiyyan355](https://github.com/Raiyyan355)
- **LinkedIn:** *(Add your LinkedIn link if you wish)*
