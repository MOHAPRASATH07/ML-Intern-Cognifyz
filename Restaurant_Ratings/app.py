import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("restaurant_rating_model.pkl", "rb"))

# Page cig

st.title(" Restaurant Rating Prediction")
st.write("Enter restaurant details below.")

# Inputs
votes = st.number_input("Votes", min_value=0, value=100)
cost = st.number_input("Average Cost for Two", min_value=0, value=500)
price_range = st.selectbox("Price Range", [1, 2, 3, 4])
cuisine_count = st.number_input("Cuisine Count", min_value=1, value=2)

# Predict button
if st.button("Predict Rating"):

    input_data = pd.DataFrame({
        'Votes': [votes],
        'Average Cost for two': [cost],
        'Price range': [price_range],
        'Cuisine Count': [cuisine_count]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Rating: ==> {prediction[0]:.2f}")