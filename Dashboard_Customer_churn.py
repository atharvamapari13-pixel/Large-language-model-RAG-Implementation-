import streamlit as st

import pandas as pd
import joblib

st.set_page_config(page_title="Marvellous Infosystem Dashboard")

st.title("Marvellous Infosystem By Piyush")
st.header("Customer Churn Prediction")
st.write("machine Learning ")

model = joblib.load("Marvellous_ML_Churn.pkl")

st.subheader("Enter Customer details")

age = st.number_input("Custome age:",min_value=1)
tenure = st.number_input("Tnure (Months)",min_value=0)
charges = st.number_input("Monthly Charges:",min_value=0)
calls = st.number_input("Support Calls:",min_value=0)
if st.button("Predict Churn"):
    new_customer = pd.DataFrame({
    "Age" : [age],
    "Tenure" : [tenure],
    "Charges" : [charges],
    "SupportCalls" : [calls]
    })

    predict = model.predict(new_customer)[0]

    if new_customer["Churn"] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is not likely to churn")

st.divider()
st.caption("Marvellous Infosystem")