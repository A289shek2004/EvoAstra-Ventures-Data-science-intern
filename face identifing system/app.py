import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load the trained model and scaler
model = load_model("face_identification_model.h5")
scaler = joblib.load("scaler.pkl")

st.title("🔐 Facial Recognition System for Employee Identification")
st.write("Upload a face image to predict whether it's Arnold Schwarzenegger or someone else.")

uploaded_file = st.file_uploader("Choose an image (simulation only)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("⚠️ Note: Using a random embedding to simulate prediction.")

    # Simulate a 128-d face embedding (replace with real one later)
    fake_embedding = np.random.rand(1, 128)
    scaled = scaler.transform(fake_embedding)
    prediction = model.predict(scaled)
    confidence = prediction[0][0]

    if confidence > 0.5:
        st.success(f"Prediction: Arnold Schwarzenegger ✅ (Confidence: {confidence:.2f})")
    else:
        st.error(f"Prediction: Not Arnold ❌ (Confidence: {1 - confidence:.2f})")
