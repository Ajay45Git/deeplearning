import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"
HEADERS = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token

# Function to query Hugging Face API for image classification
def classify_image(image_data):
    response = requests.post(API_URL, headers=HEADERS, data=image_data)

    if response.status_code == 200:
        return response.json()  # The response contains classification results
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return None

# Streamlit App
st.title("Image Classification Demo")
st.markdown("**Upload an image to classify it using the ResNet-50 model.**")

# File uploader
uploaded_file = st.file_uploader(label="Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process the image upon form submission
    with st.form(key="ClassificationForm"):
        submit = st.form_submit_button(label="Classify Image")

    if submit:
        # Convert image to binary data
        image_data = io.BytesIO()
        image.save(image_data, format="JPEG")
        image_data = image_data.getvalue()

        # Query the API
        st.info("Classifying image... Please wait.")
        response = classify_image(image_data)

        if response:
            # Display the classification results
            st.markdown("### Classification Results:")
            for result in response:  # The response is a list of top classifications
                label = result["label"]
                score = result["score"]
                st.write(f"- **{label}** with confidence **{score:.2%}**")
