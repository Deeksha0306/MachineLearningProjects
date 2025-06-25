import streamlit as st
import joblib
import numpy as np

# Loading the model
model = joblib.load("linear_regression.pkl")

# Title.
st.title("House Price Prediction 🏢💵")

# Introduction.
st.markdown("Welcome to House Price Predictor\n Enter the house details below to estimate the price of the house.")

# INPUT FIELDS.

# Bedrooms
bedroom_options = list(range(1, 34))  
bedrooms = st.selectbox("Bedrooms", bedroom_options, index=2) 

# Bathrooms
bathrooms = st.number_input("Number of Bathrooms", 
                            min_value=0.5, 
                            max_value=10.0, 
                            value=2.0, 
                            step=0.25)
bathrooms = st.slider("Bathrooms", 1, 10, 2)

# Living area
sqft_living = st.number_input("Living area (in square feet)", min_value=100, max_value=10000, value=1800)

# Floors
floors = st.number_input("Number of Floors", 
                            min_value=0.5, 
                            max_value=4.0, 
                            value=1.0, 
                            step=0.5)
floors = st.slider("Bathrooms", 1, 4, 2)

# Waterfront
waterfront_option = st.selectbox("Waterfront", ["Yes","No"])
waterfront = 1 if waterfront_option == "Yes" else 0

# View
view_options = {
    "0 - Very Poor": 0,
    "1 - Poor": 1,
    "2 - Fair": 2,
    "3 - Good": 3,
    "4 - Excellent": 4
}

selected_view_label = st.selectbox("View Quality", list(view_options.keys()))
view = view_options[selected_view_label]

# Grade
grade = st.selectbox("House Grade (1 to 13)", list(range(1, 14)), index=6)

# Above area
sqft_above = st.number_input("Sqft Above Ground (excluding basement)", min_value=1000, max_value=2000, value=1000)

# Basement area
sqft_basement = st.number_input("Sqft below Ground", min_value=0, max_value=3000, value=800)

# Latitude
lat = st.number_input("Latitude (47.1 - 47.8)", min_value=47.0, max_value=48.0, value=47.5, step=0.0001)

# Avg. Living Area of Nearby 15 Houses
sqft_living15 = st.number_input("Avg. Living Area of Nearby 15 Houses (sqft)", 
                                min_value=500, 
                                max_value=10000, 
                                value=2000, 
                                step=50)



# After the user clicks "Predict" button:
if st.button("Predict Price"):
    input_data = np.array([[bedrooms, bathrooms, sqft_living, floors, waterfront, view, grade, sqft_above, sqft_basement, lat, sqft_living15 ]])
    log_price = model.predict(input_data)[0]
    predicted_price = np.expm1(log_price)  # Convert back from log price

    # Display result
    st.success(f"💸 Estimated House Price: **${predicted_price:,.2f}**")

st.markdown("---")
st.markdown("Made with ❤️ by Deeksha during Internship")
