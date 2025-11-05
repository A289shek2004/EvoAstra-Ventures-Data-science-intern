
# Save as app.py and run: streamlit run app.py
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('/content/classification_model.h5')

st.title("Employee Face Recognition")

uploaded_file = st.file_uploader("Upload a Face Image")

if uploaded_file:
    image = Image.open(uploaded_file).resize((224,224))
    img_array = np.array(image)/255.0
    prediction = model.predict(img_array.reshape(1, 224, 224, 3))
    label = np.argmax(prediction)
    confidence = np.max(prediction)
    st.image(image)
    st.success(f"Prediction: Class {label} (Confidence: {confidence:.2f})")
