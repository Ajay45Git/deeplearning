import streamlit as st
import requests
from pathlib import Path

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
HEADERS = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token


# Function to query Hugging Face API for image captioning
def query_image_to_text(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=HEADERS, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API Error: {response.status_code}, {response.text}")
        return None


# Page Function for Image Captioning
def image_to_text_page():
    # Title and introductory text
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">📸 Image Captioning</h1>
            <p style="font-size: 18px; color: #555;">Upload an image to generate a caption using the BLIP model.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar with instructions
    st.write("**How to Use**")
    st.write("""
        1. Upload an image (JPG, JPEG, or PNG).
        2. Click **Submit** to process the image.
        3. The app will generate a caption based on the image.
    """)

    # File uploader widget
    uploaded_file = st.file_uploader(label="Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        # Process the image when the button is clicked
        with st.form(key="Upload Form", clear_on_submit=True):
            submit = st.form_submit_button(label="Generate Caption")

        if submit:
            # Save the uploaded image locally
            save_folder = Path("C:/FDP")  # Change this to your desired directory
            save_folder.mkdir(parents=True, exist_ok=True)
            save_path = save_folder / uploaded_file.name

            # Save file and display success message
            with open(save_path, mode="wb") as w:
                w.write(uploaded_file.getvalue())

            if save_path.exists():
                st.success(f"File '{uploaded_file.name}' has been successfully saved!")

                # Query Hugging Face API for image captioning
                try:
                    response = query_image_to_text(str(save_path))

                    if response:
                        # Extract and display caption
                        caption = response[0].get("generated_text", "No caption generated.")
                        st.markdown("### Generated Caption:")
                        st.write(caption)
                    else:
                        st.error("Failed to retrieve a response from the API.")

                except Exception as e:
                    st.error(f"Error while querying the API: {e}")
            else:
                st.error("Error: Failed to save the uploaded image.")

    else:
        st.warning("Please upload an image to generate a caption.")

# Call the page function to display the content
#image_to_text_page()
