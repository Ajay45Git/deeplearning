import streamlit as st
import requests
from PIL import Image, ImageDraw
import io
import os

# Hugging Face API settings
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/detr-resnet-50"
HF_TOKEN = "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"  # OR set as env var and use os.environ["HF_TOKEN"]
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "image/jpeg"
}

# Function to query Hugging Face API for object detection
def detect_objects(image_data):
    response = requests.post(API_URL, headers=HEADERS, data=image_data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return None

# Page function for object detection
def object_detection_page():
    st.markdown("""
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">🖼️ Object Detection</h1>
            <p style="color: #555;">Upload an image, and the app will detect objects in it using the Hugging Face API.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("**How to Use**")
    st.write("""
        1. Upload an image (JPEG/PNG).
        2. Press **Detect Objects** to analyze the image.
        3. Detected objects will be listed with confidence scores.
    """)

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("🔍 Detect Objects"):
            image_data = io.BytesIO()
            image.save(image_data, format="JPEG")
            image_data = image_data.getvalue()

            st.info("Detecting objects... Please wait.")
            response = detect_objects(image_data)

            if response:
                if isinstance(response, list) and len(response) > 0:
                    st.markdown("### Detected Objects:")
                    for obj in response:
                        label = obj.get("label", "Unknown")
                        score = obj.get("score", 0.0)
                        st.write(f"- **{label.capitalize()}** with confidence **{score:.2%}**")
                else:
                    st.warning("No objects detected in the image.")
            else:
                st.error("❌ Unable to detect objects. Please try again.")
    else:
        st.warning("⚠️ Please upload an image to detect objects.")

    st.markdown("""
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by Hugging Face's DETR Object Detection Model ✨</p>
        """, unsafe_allow_html=True)
