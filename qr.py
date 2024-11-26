import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# QR Code Generator Page
def qr_code_generator_page():
    st.title("URL to QR Code Generator")

    # User input for URL
    url = st.text_input("Enter the URL/Link:")

    # Select QR code size
    qr_size = st.slider("Select QR Code Size (pixels)", min_value=100, max_value=300, value=200, step=10)

    # Generate QR Code
    if st.button("Generate QR Code"):
        if url:
            # Use an online API to generate the QR code
            qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?data={url}&size={qr_size}x{qr_size}"
            response = requests.get(qr_api_url)

            if response.status_code == 200:
                # Convert the response content to an image
                img = Image.open(BytesIO(response.content))
                st.image(img, caption="Your QR Code", use_column_width=False)

                # Add a download button for the QR Code
                buf = BytesIO(response.content)
                st.download_button(
                    label="Download QR Code",
                    data=buf,
                    file_name="qr_code.png",
                    mime="image/png",
                )
            else:
                st.error("Failed to generate QR Code. Please try again later.")
        else:
            st.error("Please enter a valid URL!")