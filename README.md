
# Student Performance Predictor

This project provides an end-to-end solution for predicting students' performance using machine learning techniques. It is built to forecast a student’s math score based on key factors such as demographics, parental education, and test scores in other subjects. The application includes an interactive Flask-based web interface for real-time predictions.

---

## Table of Contents

- [Overview](#overview)  
- [Key Features](#key-features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Setup Instructions](#setup-instructions)  
- [Usage Guide](#usage-guide)  
- [Future Enhancements](#future-enhancements)  
- [Contributing](#contributing)  

---

## Overview

The **Student Performance Predictor** leverages multiple regression models to provide accurate predictions of math scores based on user input. The aim is to help identify key performance factors and provide actionable insights for improving students' academic outcomes.

---

## Key Features

1. **Exploratory Data Analysis (EDA):**
   - Insights into how demographic and academic factors influence performance.
   - Visualizations for understanding data trends.

2. **Machine Learning Pipelines:**
   - Preprocessing: Encoding categorical data, scaling numerical values, and handling missing data.
   - Model Training: Utilizes algorithms like Random Forest, XGBoost, and CatBoost.

3. **Web Application:**
   - A user-friendly web interface built with Flask to gather inputs and display predictions.
   - Styled using HTML, CSS, and Bootstrap.

4. **Deployment-Ready:**
   - Automates the training and deployment process via scripts.
   - Supports seamless model retraining and updates.

---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, Bootstrap  
- **Machine Learning:** Scikit-learn, CatBoost, XGBoost  
- **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn  
- **Deployment:** Flask (local hosting)  

---

## Project Structure

```plaintext
.
├── artifacts/              # Contains saved models and preprocessors
├── notebook/               # EDA and model training notebooks
├── src/
│   ├── components/         # Code for ingestion, transformation, and training
│   ├── pipeline/           # End-to-end training and prediction pipelines
│   ├── utils.py            # Utility functions for the project
│   ├── logger.py           # Logging setup
│   ├── exception.py        # Custom error handling
├── templates/              # HTML templates for the web interface
├── static/                 # Static assets like images and styles
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation (this file)
```

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/MohamedAklamaash/Student_Performance_Predictor.git
   cd Student_Performance_Predictor
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage Guide

1. **Training the Model:**
   - Run the training pipeline script to preprocess data and train the model:
     ```bash
     python src/pipeline/train_pipeline.py
     ```

2. **Making Predictions:**
   - Start the Flask server:
     ```bash
     python app.py
     ```
   - Open `http://localhost:5000` in a browser.
   - Input details such as gender, ethnicity, parental education, and test scores.
   - View the predicted math score on the result page.

---

## Future Enhancements

- Expand predictions to include reading and writing scores.
- Integrate deep learning techniques for improved accuracy.
- Deploy the application on a cloud platform like AWS or Heroku.

---

## Contributing

We welcome contributions! Feel free to open issues or submit pull requests to enhance the project.

---
