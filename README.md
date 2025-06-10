# Customer Churn Prediction

This project presents a deep learning-based solution to predict customer churn in the telecommunications industry. 

It includes both:

- 📈 A Jupyter notebook with exploratory data analysis, model training using TensorFlow/Keras, and evaluation.
- 🖥️ A Streamlit web app that allows interactive churn prediction based on customer input.

---

## 🧠 Overview

Customer churn prediction is a critical task for telecom companies. This project builds an artificial neural network (ANN) trained on customer demographic, account, and service usage data to determine the likelihood of churn.

---

## 🚀 Features

- Interactive Streamlit frontend for input and prediction
- Keras model trained on Telco customer churn dataset
- Feature selection based on business logic
- Backend logic abstracted for clean deployment
- Prediction confidence score display

---

## 📊 Dataset

- Source: [Kaggle – Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- Includes demographics, contract types, services, and churn label.

---
## 📈 Model Summary

- Architecture: 3-layer ANN with ReLU activations and dropout

- Preprocessing: MinMax scaling, categorical encoding

- Trained using binary cross-entropy loss

- Evaluation metrics: accuracy, confusion matrix, validation loss tracking
---

## ⚙️ Setup Instructions


```bash
1. Clone the Repository
git clone https://github.com/mpasnur/customer-churn-telco.git
cd customer-churn-telco

2. Install Python 3.10

3. Create Virtual Environment and Install Dependencies
python -m venv tf_env
.\tf_env\Scripts\activate       # Windows
# OR
source tf_env/bin/activate      # macOS/Linux

pip install -r requirements.txt

4. Run the Streamlit App
cd streamlit_app
streamlit run app.py
