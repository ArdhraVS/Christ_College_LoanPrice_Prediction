import streamlit as st
import joblib

model = joblib.load("loan_approval_decision_tree.pkl")

st.title("Loan Approval Prediction")
st.subheader("Decision Tree")

income = st.number_input("Income", min_value=0.0)
credit_score = st.number_input("Credit Score", min_value=0.0)

if st.button("Predict Loan Approval"):

    prediction = model.predict([[income, credit_score]])

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")
