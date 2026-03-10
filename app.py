# =====================================
# Email Phishing Detection App
# =====================================

import streamlit as st
import pickle

# =====================================
# Load Model and Vectorizer
# =====================================

model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Email Phishing Detection",
    page_icon="📧",
    layout="centered"
)

# =====================================
# Title
# =====================================

st.title("📧 Email Phishing Detection System")

st.write(
"""
This web application detects whether an email is **Phishing** or **Legitimate**  
using a **Machine Learning Model** trained on email datasets.
"""
)

st.write("---")

# =====================================
# Email Input Section
# =====================================

st.subheader("Enter Email Content")

email_text = st.text_area(
    "Paste the email text here:",
    height=200
)

# =====================================
# Prediction Function
# =====================================

def predict_email(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    if prediction[0] == 1:
        return "Phishing Email"
    else:
        return "Legitimate Email"

# =====================================
# Predict Button
# =====================================

if st.button("Detect Email"):

    if email_text.strip() == "":

        st.warning("⚠️ Please enter email content")

    else:

        result = predict_email(email_text)

        st.subheader("Prediction Result")

        if result == "Phishing Email":

            st.error("⚠️ This Email is a PHISHING Email")

        else:

            st.success("✅ This Email is LEGITIMATE")

# =====================================
# Example Emails Section
# =====================================

st.write("---")

st.subheader("Example Emails for Testing")

st.write("**Example Phishing Email:**")

st.code(
"""
Dear user,

Your bank account has been suspended.
Please click the link below to verify your account immediately.

http://fakebank-login.com
"""
)

st.write("**Example Legitimate Email:**")

st.code(
"""
Hello Team,

Please find the meeting agenda attached for tomorrow's discussion.

Best regards,
Manager
"""
)

# =====================================
# Project Information
# =====================================

st.write("---")

st.subheader("Project Information")

st.write(
"""
Project: Email Phishing Detection using Machine Learning  

Algorithm Used:
- TF-IDF Vectorization
- Random Forest Classifier

Purpose:
Detect phishing emails to protect users from cyber attacks.
"""
)

st.write("---")

st.write("Developed for Final Year Project")
