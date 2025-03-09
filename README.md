# 🍄 Mushroom Classification ML Project
This repository contains a Machine Learning project that classifies mushrooms as *edible* or *poisonous* based on various features. The model is implemented in Python using Jupyter Notebook.

## Project Overview
This project aims to predict whether a mushroom is edible or poisonous based on various categorical features such as cap shape, odor, gill size, and habitat. The dataset used is a well-known mushroom dataset from the *UCI Machine Learning Repository*.

## Technologies Used
- *Programming Language*: Python
- *Libraries*:
  - Pandas & NumPy ➔ Data Processing
  - Scikit-learn ➔ Machine Learning Models
  - Matplotlib & Seaborn ➔ Data Visualization
  - Flask/Streamlit (if deployed) ➔ Web App Deployment

## 📚 Dataset Information
- *Source*: [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/mushroom)
- *Number of Instances*: 8,124
- *Number of Features*: 22 categorical attributes
- *Target Variable*: class
  - e ➔ Edible
  - p ➔ Poisonous

## 📝 Project Structure

/mushroom-classification
│── data/                   # Dataset
│── models/                 # Trained models 
│── notebook/               # Jupyter Notebooks
│── app/                    # Deployment files (Flask)
│── requirements.txt        # Python dependencies
│── README.md               # Project Documentation

     

## 📊 Model Performance
- *Model Used*: Logistic Regression/SVC/DecisionTree/RandomForestClassifier 
- *Accuracy*: 95%+ 
- *Evaluation Metrics*:
  - Precision, Recall, F1-score
  - Confusion Matrix
