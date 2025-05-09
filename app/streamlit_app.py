import streamlit as st
import cv2
import numpy as np
from utils.preprocessing import preprocess_image

st.title("Damaged Car Image Preprocessing App")

uploaded_file = st.file_uploader("Upload a damaged car image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, channels="BGR", caption="Original Image")

    processed_image = preprocess_image(image)

    st.image(processed_image, channels="BGR", caption="Preprocessed Image")
