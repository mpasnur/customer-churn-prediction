import streamlit as st
import tensorflow as tf
import numpy as np
from backend import initialize_backend_model, predict_score
import json

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("Customer Churn Prediction")

# Load backend model
statusCode, jsonResponse = initialize_backend_model()
response = json.loads(jsonResponse)
if statusCode != 200:
    st.error(f'{response["status"]}: {response["message"]}')
    st.stop()

with st.form("churn_form"):
    st.subheader("Customer Profile")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        isSeniorCitizen = st.checkbox("Senior Citizen")
        isPartner = st.checkbox("Has Partner")
        isDependents = st.checkbox("Has Dependents")

    with col2:
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=30, step=5)
        monthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0, step=5.0)
        totalCharges = st.number_input("Total Charges ($)", min_value=0.0, max_value=9000.0, value=2000.0, step=100.0)

    st.subheader("Phone & Internet Services")

    col3, col4 = st.columns(2)

    with col3:
        isPhoneService = st.checkbox("Phone Service")
        isMultipleLines = st.checkbox("Multiple Lines") if isPhoneService else False

    with col4:
        internetService = st.selectbox("Internet Service", ["No", "DSL", "Fiber optic"], index=0)

    if internetService != "No":
        col5, col6 = st.columns(2)
        with col5:
            isOnlineSecurity = st.checkbox("Online Security")
            isOnlineBackup = st.checkbox("Online Backup")
            isDeviceProtected = st.checkbox("Device Protection")
        with col6:
            isTechSupport = st.checkbox("Technical Support")
            isStreamingTV = st.checkbox("Streaming TV")
            isStreamingMovies = st.checkbox("Streaming Movies")
    else:
        isOnlineSecurity = isOnlineBackup = isDeviceProtected = isTechSupport = isStreamingTV = isStreamingMovies = False

    st.subheader("Billing Preferences")

    col7, col8 = st.columns(2)
    with col7:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    with col8:
        paymentMethod = st.selectbox("Payment Method", [
            "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
        ])

    isPaperless = st.checkbox("Paperless Billing")

    submit = st.form_submit_button("Predict")

if submit:
    data = [
        isSeniorCitizen,
        tenure,
        monthlyCharges,
        totalCharges,
        1 if gender == 'Male' else 0,
        isPartner,
        isDependents,
        1 if contract == 'One year' else 0,
        1 if contract == 'Two year' else 0,
        isPaperless,
        1 if paymentMethod == 'Credit card (automatic)' else 0,
        1 if paymentMethod == 'Electronic check' else 0,
        1 if paymentMethod == 'Mailed check' else 0,
        isPhoneService,
        isMultipleLines,
        1 if internetService == 'Fiber optic' else 0,
        1 if internetService == 'No' else 0,
        isOnlineSecurity,
        isOnlineBackup,
        isDeviceProtected,
        isTechSupport,
        isStreamingTV,
        isStreamingMovies
    ]

    # Make prediction
    statusCode, jsonResponse = predict_score(json.dumps(data))
    response = json.loads(jsonResponse)

    st.divider()

    if statusCode != 200:
        st.error(f'{response["status"]}: {response["message"]}')
    else:
        st.subheader("Prediction Result")
        prediction = response["prediction"]

        if prediction > 0.5:
            st.success(f"The customer is likely to **stay** (score: {prediction:.2f})", icon=None)
        else:
            st.warning(f"The customer is likely to **churn** (score: {prediction:.2f})", icon=None)
