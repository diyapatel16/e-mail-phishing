import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Email Phishing Detector", layout="wide")

# ===============================
# STYLE
# ===============================
st.markdown("""
<style>
.card {
    background: linear-gradient(145deg, #ffffff, #f2f2f2);
    border-radius: 18px;
    padding: 28px;
    box-shadow:
        8px 8px 18px rgba(0,0,0,0.12),
       -8px -8px 18px rgba(255,255,255,0.9);
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# LOAD MODEL
# ===============================
@st.cache_resource
def load_model():
    model = pickle.load(open("phishing_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# ===============================
# NAVIGATION
# ===============================
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Use Cases", "Charts", "Detection", "About"]
)

# ===============================
# HOME PAGE
# ===============================
if page == "Home":

    st.title("📧 Email Phishing Detection System")

    st.write("""
This application detects whether an email is **Phishing or Legitimate**
using a **Machine Learning model**.
""")

# ===============================
# USE CASES
# ===============================
elif page == "Use Cases":

    st.title("📌 Use Cases")

    st.markdown("""
- Cybersecurity monitoring  
- Email spam filtering  
- Corporate email protection  
- Academic ML research  
""")

# ===============================
# CHARTS
# ===============================
elif page == "Charts":

    st.title("📊 Model Insights")

    chart_data = pd.DataFrame({
        "Email Type": ["Phishing", "Legitimate"],
        "Count": [40, 60]
    })

    st.bar_chart(chart_data.set_index("Email Type"))

# ===============================
# DETECTION
# ===============================
elif page == "Detection":

    st.title("🔍 Email Phishing Detection")

    email_text = st.text_area("Enter Email Content")

    if st.button("Detect Email"):

        if email_text.strip() == "":
            st.warning("Please enter email text")

        else:
            email_vec = vectorizer.transform([email_text])
            prediction = model.predict(email_vec)[0]

            if prediction == 1:
                st.error("⚠️ PHISHING EMAIL DETECTED")
            else:
                st.success("✅ LEGITIMATE EMAIL")

# ===============================
# ABOUT
# ===============================
elif page == "About":

    st.title("About Project")

    st.write("""
This project detects phishing emails using TF-IDF vectorization
and a trained machine learning classification model.
""")
