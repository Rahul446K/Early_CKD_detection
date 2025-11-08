# Early_CKD_detection
Machine Learning–based web app for early detection of Chronic Kidney Disease (CKD)




🩺 Early Chronic Kidney Disease (CKD) Detection

A machine learning–powered web app for early detection of Chronic Kidney Disease (CKD).
The app allows users to input clinical test values and instantly get a prediction on whether a person is likely to have CKD.

🚀 Live Web App

📌 Overview

Early diagnosis of CKD helps prevent kidney failure and improves patient outcomes.
This project uses a trained ML pipeline to analyze medical features like blood pressure, hemoglobin, blood glucose, and other indicators to predict CKD risk.
The model was trained, saved, and deployed using Streamlit for an interactive web experience.

🧠 Features

Interactive and clean Streamlit interface

Real-time CKD prediction using a trained model

Categorized input fields for better usability

Smooth gradient and centered layout for better visuals

🧩 Tech Stack

Python
Pandas, NumPy, scikit-learn, joblib
Streamlit (for UI and deployment)
Git & GitHub (for version control)


⚙️ How to Run Locally

Clone the repository

git clone https://github.com/Rahul446K/Early_CKD_detection.git
cd Early_CKD_detection


Create and activate virtual environment

python -m venv env
env\Scripts\activate     # For Windows


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


Open the local URL shown in the terminal (usually http://localhost:8501).




📊 Dataset

The dataset used for training includes patient details such as:
Age, Blood Pressure, Specific Gravity
Sugar, Albumin, Hemoglobin, Serum Creatinine
Diabetes, Hypertension, Anemia, and more



🧪 Model Details

Handled missing and categorical data during preprocessing
Tested multiple classifiers and selected the best performing one
Model stored as ckd_model_bundle.joblib for deployment
Predictions are made using the trained ML pipeline


🌐 Deployment

The project is deployed using Streamlit Cloud and can be accessed here:
🔗 https://rahul446k-early-ckd-detection.streamlit.app/
