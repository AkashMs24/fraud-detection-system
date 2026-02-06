import streamlit as st
import requests

API_URL = "https://fraud-detection-system-2-7ake.onrender.com/predict_fraud"

st.set_page_config(page_title="Fraud Detection UI", layout="centered")

st.title("💳 Fraud Detection System")
st.write("Enter transaction details to assess fraud risk.")

with st.form("fraud_form"):
    Time = st.number_input("Time", value=0.0)
    Amount = st.number_input("Amount", value=0.0)

    st.subheader("PCA Features (V1 – V28)")
    features = {}
    for i in range(1, 29):
        features[f"V{i}"] = st.number_input(f"V{i}", value=0.0)

    submit = st.form_submit_button("Check Fraud Risk")

if submit:
    payload = {
        "Time": Time,
        "Amount": Amount,
        **features
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        st.success("Prediction Successful")
        st.write("### Results")
        st.write(f"**Fraud Probability:** {result['fraud_probability']}")
        st.write(f"**Risk Level:** {result['risk_level']}")

    except Exception as e:
        st.error("API call failed")
        st.write(e)
