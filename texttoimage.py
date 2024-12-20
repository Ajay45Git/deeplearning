import streamlit as st
import requests
from PIL import Image
import io

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token


# Function to query Hugging Face API for image generation
def generate_image_from_text(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        # Return image as a PIL object
        return Image.open(io.BytesIO(response.content))
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return None


# Page Function for Text-to-Image
def text_to_image_page():
    # Title and introduction
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">🎨 Text-to-Image Generator</h1>
            <p style="font-size: 18px; color: #555;">Generate an image based on your description using the Stable Diffusion XL model.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar instructions
    st.write("**How to Use**")
    st.write("""
        1. Enter a text prompt that describes the image you want.
        2. Click **Generate Image**.
        3. The app will generate the image and display it below.
    """)

    # Input text prompt
    prompt = st.text_input(label="Describe the Image", placeholder="e.g., A sunset over the ocean...")

    # Generate image when button is clicked
    if st.button("🖼️ Generate Image"):
        if prompt.strip():
            st.info("Generating the image. Please wait...")
            image = generate_image_from_text(prompt)

            if image:
                # Display the generated image
                st.image(image, caption="Generated Image", use_container_width=True)

                # Option to download the image
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                buf.seek(0)
                st.download_button(
                    label="Download Image",
                    data=buf,
                    file_name="generated_image.png",
                    mime="image/png"
                )
        else:
            st.warning("Please enter a text prompt to generate an image.")

    # Footer credit
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by Hugging Face's Stable Diffusion XL Model ✨</p>
        """,
        unsafe_allow_html=True,
    )

# Call the page function
#text_to_image_page()
