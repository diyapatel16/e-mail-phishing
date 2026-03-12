import streamlit as st
import pandas as pd
import pickle
import numpy as np

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Email Phishing Detector", layout="wide")

# ===============================
# STYLE
# ===============================
st.markdown("""
<style>
body {
    background-color: #ffffff;
}
.card {
    background: linear-gradient(145deg, #ffffff, #f2f2f2);
    border-radius: 18px;
    padding: 28px;
    box-shadow:
        8px 8px 18px rgba(0,0,0,0.12),
       -8px -8px 18px rgba(255,255,255,0.9);
    margin-bottom: 30px;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# ===============================
# LOAD MODEL + VECTORIZER
# ===============================
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

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

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("📧 Email Phishing Detection System")

    st.write("""
    This application detects whether an email is **Phishing or Legitimate**
    using a **machine learning classification model**.

    The system analyzes the **email text content** and predicts whether
    the message is attempting a phishing attack.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# USE CASES
# ===============================
elif page == "Use Cases":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("📌 Use Cases")

    st.markdown("""
    - 🔐 Cybersecurity monitoring  
    - 📧 Email spam filtering  
    - 🏢 Corporate email protection  
    - 🎓 Academic machine learning research  
    - 💻 Phishing attack detection systems  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# CHARTS PAGE
# ===============================
elif page == "Charts":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("📊 Model Insights")

    st.subheader("Phishing vs Legitimate Distribution")

    chart_data = pd.DataFrame({
        "Email Type": ["Phishing", "Legitimate"],
        "Example Count": [40, 60]
    })

    st.bar_chart(chart_data.set_index("Email Type"))

    st.subheader("Model Decision Concept")

    concept = pd.DataFrame({
        "Factor": [
            "Suspicious Links",
            "Urgent Language",
            "Fake Domains",
            "Password Requests",
            "Financial Threats"
        ],
        "Influence": [90, 80, 85, 95, 75]
    })

    st.bar_chart(concept.set_index("Factor"))

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# EMAIL DETECTION PAGE
# ===============================
elif page == "Detection":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("🔍 Email Phishing Detection")

    email_text = st.text_area(
        "Enter Email Content",
        height=200
    )

    if st.button("🚀 Detect Email"):

        if email_text.strip() == "":
            st.warning("Please enter email content")

        else:

            email_vec = vectorizer.transform([email_text])

            prediction = model.predict(email_vec)[0]

            st.subheader("Prediction Result")

            if prediction == 1:
                st.error("⚠️ PHISHING EMAIL DETECTED")
                st.metric("Risk Level", "High")
            else:
                st.success("✅ LEGITIMATE EMAIL")
                st.metric("Risk Level", "Low")

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# ABOUT PAGE
# ===============================
elif page == "About":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.title("ℹ️ About This Project")

    st.write("""
    This project detects phishing emails using a **machine learning model**
    trained on email datasets.

    Email text is converted into numerical features using
    **TF-IDF vectorization**, and the trained classification model
    predicts whether the message is phishing or legitimate.

    The system is deployed using Streamlit for real-time detection.
    """)

    st.markdown("</div>", unsafe_allow_html=True)
