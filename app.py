
import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl","rb"))

# Title
st.title("🏠 Real Estate Investment Advisor")

st.write("Enter property details")

# Inputs from user
bhk = st.slider("BHK",1,5,2)

size = st.number_input(
    "Size in SqFt",
    min_value=500,
    max_value=10000,
    value=1200
)

floor = st.number_input(
    "Floor No",
    min_value=0,
    max_value=50,
    value=1
)

total_floors = st.number_input(
    "Total Floors",
    min_value=1,
    max_value=100,
    value=5
)

age = st.number_input(
    "Age of Property",
    min_value=0,
    max_value=50,
    value=5
)

# Convert input into dataframe
input_data = pd.DataFrame({
    "BHK":[bhk],
    "Size_in_SqFt":[size],
    "Floor_No":[floor],
    "Total_Floors":[total_floors],
    "Age_of_Property":[age]
})

# Prediction button
if st.button("Predict Price"):

    current_price = model.predict(input_data)[0]

    # demo logic
    if size < 900 or age > 20:
        growth_rate = 0.03
    else:
        growth_rate = 0.08

    future_price = current_price * (1 + growth_rate)**5

    st.success(f"Current Price: ₹ {current_price:.2f} Lakhs")

    st.info(f"Price after 5 years: ₹ {future_price:.2f} Lakhs")

    if future_price > current_price * 1.30:
        st.success("Good Investment ✅")
    else:
        st.warning("Moderate Investment ⚠")