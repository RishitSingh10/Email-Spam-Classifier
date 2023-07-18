import streamlit as st
import pickle
from preprocessing import text_process

with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

# Check if input is provided
if st.button('Predict'):

    if input_sms:
        # 1. Use pipeline to predict
        prediction = pipeline.predict([input_sms])[0]

        # 2. Display
        if prediction == 'spam':
            st.header("Spam")
        else:
            st.header("Not Spam")