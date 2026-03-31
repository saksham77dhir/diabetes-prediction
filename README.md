# 🩺 Diabetes Prediction Web App

This project is a **Machine Learning-based web application** built using **Streamlit** that predicts whether a person is diabetic or non-diabetic based on medical input parameters.

---

## 📌 Overview

The application takes **8 health-related inputs** from the user and uses a trained ML model to predict diabetes.

### ✨ Highlights
- Fast and real-time predictions  
- Simple and interactive UI  
- End-to-end ML workflow (training → deployment)

---

## ⚙️ Technologies Used

- Python  
- NumPy  
- Scikit-learn  
- Streamlit   

---

## 📊 Features Used for Prediction

The model uses the following input features:

1. Pregnancies  
2. Glucose Level  
3. Blood Pressure  
4. Skin Thickness  
5. Insulin Level  
6. BMI (Body Mass Index)  
7. Diabetes Pedigree Function  
8. Age  

---

## 🧠 Machine Learning Model

- Model: SVM 
- Preprocessing:
  - Feature scaling using **StandardScaler**

Both model and scaler are saved as `.pkl` files and loaded in the Streamlit app.

---
