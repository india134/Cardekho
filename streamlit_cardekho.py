import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('car_price_model.pkl')

# Title of the Streamlit app
st.title("Car Price Prediction")

# Input fields for the user to provide car details
age = st.number_input("How old is the car (in years)?", min_value=0, step=1)
seating_capacity = st.number_input("Seating Capacity", min_value=1, max_value=10, step=1)
fuel_tank_capacity = st.number_input("Fuel Tank Capacity (liters)", min_value=10, max_value=100, step=1)
transmission = st.selectbox("Transmission Type", options=["Automatic", "Manual"])
fuel_type = st.selectbox("Fuel Type", options=['CNG', 'CNG + CNG', 'Diesel', 'Electric', 'Hybrid', 'LPG', 'Petrol', 'Petrol + CNG', 'Petrol + LPG'])
owner_type = st.selectbox("Owner Type", options=["Corporate", "Individual"])
drivetrain = st.selectbox("Drive Type", options=["AWD", "FWD", "RWD"])

# Additional input for power and torque to calculate Combined Power HP
power = st.number_input("Power (kW)", min_value=0.0, step=0.1)
torque = st.number_input("Torque (Nm)", min_value=0.0, step=0.1)
rpm = st.number_input("RPM", min_value=500, step=100)

# Calculate combined_power_hp and power_rpm_ratio
combined_power_hp = (torque * power) / 745.7
power_rpm_ratio = power / rpm

# Prepare the input for the model (with additional features set to default values)
model_input = np.array([[age, seating_capacity, fuel_tank_capacity, 
                         1 if transmission == "Automatic" else 0,  # Encoding transmission
                         # Encoding fuel type (dummy variables for fuel type)
                         1 if fuel_type == 'CNG' else 0, 1 if fuel_type == 'Diesel' else 0, 1 if fuel_type == 'Petrol' else 0,
                         1 if owner_type == "Corporate" else 0,  # Encoding owner type
                         1 if drivetrain == "AWD" else 0, 1 if drivetrain == "FWD" else 0, 1 if drivetrain == "RWD" else 0,
                         combined_power_hp, power_rpm_ratio,
                         # Fill in the rest of the features (16 more) with default values (e.g., 0)
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Predict button
if st.button("Predict Price"):
    # Make the prediction using the loaded model
    predicted_price = model.predict(model_input)
    st.success(f"The predicted price of the car is: ₹{predicted_price[0]:,.2f}")
