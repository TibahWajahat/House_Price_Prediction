import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6f9;
}
.title {
    font-size:40px;
    font-weight:bold;
    color:#2E86C1;
}
.subtext {
    font-size:18px;
    color:gray;
}
.stButton>button {
    background-color:#2E86C1;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:3em;
    width:100%;
}
.stButton>button:hover {
    background-color:#1B4F72;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="title">🏠 Smart House Price Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Enter house details and get AI based price prediction</p>', unsafe_allow_html=True)

st.write("")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model/model.pkl", "rb"))

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Basic House Details")

    area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=1500)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

with col2:
    st.subheader("🏡 Additional Details")

    stories = st.number_input("Number of Stories", min_value=1, max_value=5, value=1)
    parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)

st.write("")
st.write("")

# ---------------- PREDICTION BUTTON ----------------
if st.button("🚀 Predict House Price"):

    input_data = np.array([[area, bedrooms, bathrooms, stories, parking]])

    prediction = model.predict(input_data)

    st.markdown("---")
    st.success(f"💰 Estimated House Price: ₹ {prediction[0]:,.2f}")
    st.balloons()