import streamlit as st
import requests
from PIL import Image
import io
import os

# Hugging Face API URL and headers
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/detr-resnet-50"
HF_TOKEN = "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" 
headers = {
    "Authorization": f"Bearer {os.environ[HF_TOKEN]}",
    "Content-Type": "image/jpeg"
}

# Function to query the model
def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

# Streamlit UI
st.title("Object Detection using DETR (facebook/detr-resnet-50)")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    with st.spinner("Running inference..."):
        output = query(img_bytes)

    st.subheader("Model Predictions")
    st.json(output)





