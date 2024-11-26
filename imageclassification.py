import streamlit as st
import requests
from PIL import Image


# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"
headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token


# Function to query the Hugging Face API with an image
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


# Function to display Image Recognition tab
def image_classification_page():
    # Brief Introduction
    st.write("""
    ## Image Classification with ResNet-50
    Upload an image (single object), and our pre-trained **ResNet-50** model will recognize its contents. 
    The model will return the top predictions with confidence scores.
    """)

    st.write("Upload an image to get recognized content using the Hugging Face model.")

    # File uploader for image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Check if an image has been uploaded
    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)  # Updated parameter

        # Convert image to RGB (if not already in that format)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Save the image locally
        image.save("uploaded_image.jpg")

        # Button to trigger recognition
        if st.button("Recognize Image"):
            st.write("Recognizing the image...")

            # Call the Hugging Face API to get predictions
            output = query("uploaded_image.jpg")

            # Extract labels and confidence scores from the output
            labels = [item['label'] for item in output]
            scores = [item['score'] for item in output]

            # Display the predictions as an ordered list with scores
            st.write("### Predictions:")
            for idx, (label, score) in enumerate(zip(labels, scores), start=1):
                st.write(f"- **{label}** with confidence **{score:.2%}**")

