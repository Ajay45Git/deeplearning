'''
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
    # Title and Introduction
    st.markdown("""
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">🖼️ Image Classification</h1>
            <p style="font-size: 18px; color: #555;">Upload an image, and our pre-trained <b>ResNet-50</b> model will recognize its contents. The model will return the top predictions with confidence scores.</p>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar Instructions
    st.write("**How to Use**")
    st.write("""
        1. Upload an image (JPG, JPEG, PNG).
        2. Click **Recognize Image** to classify the image.
        3. The app will display the predictions with their confidence scores.
    """)

    # File uploader widget
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # If image is uploaded
    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert image to RGB (if not already in that format)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Save the image locally
        save_path = "uploaded_image.jpg"
        image.save(save_path)

        # Button to trigger recognition
        if st.button("Recognize Image"):
            st.write("Recognizing the image...")

            # Call the Hugging Face API to get predictions
            try:
                output = query(save_path)

                if output:
                    # Extract labels and confidence scores from the output
                    labels = [item['label'] for item in output]
                    scores = [item['score'] for item in output]

                    # Display the predictions as an ordered list with scores
                    st.write("### Top Predictions:")
                    for idx, (label, score) in enumerate(zip(labels, scores), start=1):
                        st.write(f"- **{label}** with confidence **{score:.2%}**")
                else:
                    st.error("Failed to retrieve predictions from the API.")

            except Exception as e:
                st.error(f"Error occurred: {e}")

    else:
        st.warning("Please upload an image to recognize.")

# Call the functihon to display the image classification page
#image_classification_page()
'''










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
    # Title and Introduction  
    st.markdown("""  
        <div style="text-align: center;">  
            <h1 style="color: #4CAF50;">🖼️ Image Classification</h1>  
            <p style="font-size: 18px; color: #555;">Upload an image, and our pre-trained <b>ResNet-50</b> model will recognize its contents. The model will return the top predictions with confidence scores.</p>  
        </div>  
    """, unsafe_allow_html=True)  
  
    # Sidebar Instructions  
    st.write("**How to Use**")  
    st.write("""  
        1. Upload an image (JPG, JPEG, PNG).  
        2. Click **Recognize Image** to classify the image.  
        3. The app will display the predictions with their confidence scores.  
    """)  
  
    # File uploader widget  
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])  
  
    # If image is uploaded  
    if uploaded_image is not None:  
        # Display the uploaded image  
        image = Image.open(uploaded_image)  
        st.image(image, caption="Uploaded Image", use_container_width=True)  
  
        # Convert image to RGB (if not already in that format)  
        if image.mode != 'RGB':  
            image = image.convert('RGB')  
  
        # Save the image locally  
        save_path = "uploaded_image.jpg"  
        image.save(save_path)  
  
        # Button to trigger recognition  
        if st.button("Recognize Image"):  
            st.write("Recognizing the image...")  
  
            # Call the Hugging Face API to get predictions  
            try:  
                output = query(save_path)  
                st.write("API raw output:", output)  # For debugging  
  
                if isinstance(output, list) and all(isinstance(item, dict) and 'label' in item and 'score' in item for item in output):  
                    st.write("### Top Predictions:")  
                    for idx, item in enumerate(output, start=1):  
                        st.write(f"- **{item['label']}** with confidence **{item['score']:.2%}**")  
                elif isinstance(output, dict) and "error" in output:  
                    st.error(f"API Error: {output['error']}")  
                else:  
                    st.error("Unexpected response format from API.")  
  
            except Exception as e:  
                st.error(f"Error occurred: {e}")  
  
    else:  
        st.warning("Please upload an image to recognize.")
