import streamlit as st
import requests
from pathlib import Path

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
HEADERS = {"Authorization": "Bearer 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"}


# Function to query Hugging Face API
def query_image_to_text(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=HEADERS, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API Error: {response.status_code}, {response.text}")
        return None


# Page Function for Image to Text
def image_to_text_page():
    st.title("Image Captioning")
    st.markdown("**Please Upload an Image File:**")

    uploaded_file = st.file_uploader(label="Upload file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Form submission for processing the image
        with st.form(key="Upload Form", clear_on_submit=True):
            submit = st.form_submit_button(label="Submit")

        if submit:
            # Save the uploaded file locally
            save_folder = Path("C:/FDP")
            save_folder.mkdir(parents=True, exist_ok=True)
            save_path = save_folder / uploaded_file.name

            with open(save_path, mode="wb") as w:
                w.write(uploaded_file.getvalue())

            if save_path.exists():
                st.success(f"File '{uploaded_file.name}' is successfully saved!")

                # Query the Hugging Face API
                try:
                    response = query_image_to_text(str(save_path))

                    if response:
                        # If the response is a list, extract the first result
                        caption = response[0].get("generated_text", "No caption generated.")

                        # Display the generated caption
                        st.markdown("**Generated Caption for the Image:**")
                        st.write(caption)
                    else:
                        st.error("Failed to retrieve a response from the API.")

                except Exception as e:
                    st.error(f"Error while querying the API: {e}")
