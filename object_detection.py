import streamlit as st
import requests
from PIL import Image, ImageDraw
import io

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
HEADERS = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token


# Function to query Hugging Face API for object detection
def detect_objects(image_data):
    response = requests.post(API_URL, headers=HEADERS, data=image_data)

    if response.status_code == 200:
        return response.json()  # This will be a list of objects
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return None


# Page function for object detection
def object_detection_page():
    st.title("Object Detection")
    st.markdown("**Upload an image(which has multiple object), and the app will detect objects in it using the Hugging Face API.**")

    # File uploader
    uploaded_file = st.file_uploader(label="Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Process the image upon form submission
        with st.form(key="ObjectDetectionForm"):
            submit = st.form_submit_button(label="Detect Objects")

        if submit:
            # Convert image to binary data
            image_data = io.BytesIO()
            image.save(image_data, format="JPEG")
            image_data = image_data.getvalue()

            # Query the API
            st.info("Detecting objects... Please wait.")
            response = detect_objects(image_data)

            if response:
                # Iterate through the list of detected objects
                if len(response) > 0:
                    st.markdown("### Detected Objects:")
                    for obj in response:
                        label = obj["label"]
                        score = obj["score"]
                        st.write(f"- **{label.capitalize()}** with confidence **{score:.2%}**")
                else:
                    st.warning("No objects detected in the image.")
