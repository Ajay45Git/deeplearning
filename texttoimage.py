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
    st.title("Text-to-Image Generator")
    st.markdown("**Enter a text prompt to create an image:**")

    # Input text prompt
    prompt = st.text_input(label="Text Prompt", placeholder="Describe the image you want to generate...")

    # Form submission
    if st.button("Generate Image"):
        if prompt:
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
