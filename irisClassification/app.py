import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("IRIS FLOWER CLASSIFICATION. 🌸🌺🌹🌻")
st.write("Enter the following informations to predict the type of flower.")
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.3)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]

    species_map = {0: 'Setosa 🌼', 1: 'Versicolor 🌷', 2: 'Virginica 🌹'}
    predicted_species = species_map[prediction]

    st.success(f"✨ The predicted Iris species is: **{predicted_species}**")

st.markdown("---")