import streamlit as st
import numpy as np
import joblib
import joblib
from sklearn.ensemble import RandomForestRegressor

import joblib
from sklearn.ensemble import RandomForestRegressor

# Function to load and combine split model parts
import joblib

import joblib
from sklearn.ensemble import RandomForestRegressor

# Function to load and combine split model parts
def load_split_model(part1_path, part2_path):
    # Load both parts
    with open(part1_path, "rb") as f1:
        part1 = joblib.load(f1)
    with open(part2_path, "rb") as f2:
        part2 = joblib.load(f2)
    
    # Combine the parts into a single RandomForest model
    combined_model = RandomForestRegressor()
    combined_model.estimators_ = part1 + part2
    combined_model.n_outputs_ = 1  # Manually setting the attribute
    return combined_model

# Load the split model
model = load_split_model("model_part1.pkl", "model_part2.pkl")








# Page Title
st.title("Car Price Prediction App")

# Input Features
st.sidebar.header("Input Features")
year = st.sidebar.number_input("Year of Manufacture", min_value=2000, max_value=2025, step=1)
location = st.sidebar.selectbox("Location", ["City 1", "City 2", "City 3", "City 4"])
seating_capacity = st.sidebar.number_input("Seating Capacity", min_value=2, max_value=10, step=1)
fuel_tank_capacity = st.sidebar.number_input("Fuel Tank Capacity (Liters)", min_value=10.0, max_value=100.0, step=0.1)
transmission = st.sidebar.selectbox("Transmission", ["Automatic", "Manual"])
fuel_type = st.sidebar.selectbox("Fuel Type", ["CNG", "CNG + CNG", "Diesel", "Electric", "Hybrid", "LPG", "Petrol", "Petrol + CNG", "Petrol + LPG"])
ownership = st.sidebar.selectbox("Ownership Type", ["Commercial Registration", "Corporate", "Individual"])
drive_type = st.sidebar.selectbox("Drive Type", ["AWD", "FWD", "RWD"])
combined_power_hp = st.sidebar.number_input("Combined Power (HP)", min_value=50, max_value=500, step=1)
power_rpm_ratio = st.sidebar.number_input("Power-to-RPM Ratio", min_value=0.0, max_value=10.0, step=0.1)
distance_per_year = st.sidebar.number_input("Distance Driven per Year (km)", min_value=1000, max_value=100000, step=1000)
volume = st.sidebar.number_input("Volume (cubic meters)", min_value=1.0, max_value=50.0, step=0.1)

# Adding a placeholder for the 29th feature
new_feature = st.sidebar.number_input("New Feature (custom input)", min_value=0.0, max_value=100.0, step=0.1)

# Encoding categorical inputs
location_features = [1 if location == f"City {i+1}" else 0 for i in range(4)]
transmission_features = [1 if transmission == "Automatic" else 0, 1 if transmission == "Manual" else 0]
fuel_type_features = [1 if fuel_type == ft else 0 for ft in ["CNG", "CNG + CNG", "Diesel", "Electric", "Hybrid", "LPG", "Petrol", "Petrol + CNG", "Petrol + LPG"]]
ownership_features = [1 if ownership == ow else 0 for ow in ["Commercial Registration", "Corporate", "Individual"]]
drive_type_features = [1 if drive_type == dt else 0 for dt in ["AWD", "FWD", "RWD"]]

# Combine all features
features = (
    [year]
    + location_features
    + [seating_capacity]
    + [fuel_tank_capacity]
    + transmission_features
    + fuel_type_features
    + ownership_features
    + drive_type_features
    + [combined_power_hp]
    + [power_rpm_ratio]
    + [distance_per_year]
    + [volume]
    + [new_feature]  # Adding the missing 29th feature
)

# Count the features for validation
feature_count = len(features)
st.write(f"Feature Count: {feature_count} (Expected: 29)")

# Validate feature count
if feature_count != 29:
    st.error(f"Expected 29 features, but got {feature_count}. Please check inputs!")
else:
    # Add a Predict Button
    if st.button("Predict Price"):
        # Predict the scaled price
        scaled_price = model.predict([features])[0]

        # Define scaler mean and std for the target variable (Price)
        # Replace these values with the actual mean and std used during training
        price_mean = 500000  # Example: Replace with actual mean of price
        price_std = 250000   # Example: Replace with actual std of price

        # Inverse transform the scaled price to get the real price
        real_price = scaled_price * price_std + price_mean

        # Display the real price
        st.success(f"The predicted car price is: ₹{real_price:,.2f}")
