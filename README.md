This repository contains a machine learning-powered web application that predicts car prices based on multiple input features. The application uses a Random Forest Regressor trained on a dataset of cars and is deployed using Streamlit.

Features
App Features
User Input:
Users can input various car features (e.g., Year, Fuel Type, Location, etc.) through an interactive web interface.
Prediction:
The app predicts the car's price based on the inputs.
Real Price Output:
The predicted price is displayed after being inversely transformed from the scaled value used in model training.
Supported Features (29 Features Total)
The following features are considered by the app for prediction:

Year
Location
Seating Capacity
Fuel Tank Capacity
Transmission (Automatic, Manual)
Fuel Type (CNG, Diesel, Petrol, Electric, etc.)
Ownership Type (Owner Encoded)
Registration Type (Commercial, Corporate, Individual)
Drive Type (AWD, FWD, RWD)
Engine Specifications (Combined Power HP, Power-RPM Ratio)
Distance Driven per Year
Vehicle Volume


Project Workflow
1. Dataset
It contains detailed information about cars such as model year, mileage, fuel type, transmission, ownership, and price.

3. Exploratory Data Analysis (EDA)
Analyzed data distribution for numerical features such as price, mileage, and fuel capacity using boxplots and histograms.
Correlation analysis revealed key features impacting car price.
Identified and handled outliers to improve model performance.
Engineered additional features (e.g., power-rpm-ratio, distance-driven-per-year) to enhance prediction accuracy.

5. Data Preprocessing
Handled missing values using mean/mode imputation.
Encoded categorical variables using one-hot encoding and label encoding.
Scaled numerical features using StandardScaler for uniformity.

7. Model Training
Algorithm Used: Random Forest Regressor
Chosen for its robustness to outliers and ability to capture non-linear relationships.
Hyperparameter Tuning:
Used GridSearchCV to optimize hyperparameters such as the number of trees and depth.

Performance Metrics:
Achieved high R² score on test data, indicating good predictive power.





