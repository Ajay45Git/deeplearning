import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# QR Code Generator Page
def qr_code_generator_page():
    # Title and introduction
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">🔗 URL to QR Code Generator</h1>
            <p style="color: #555;">Easily convert any URL into a scannable QR Code.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # User input for URL
    st.markdown("### 🌐 Enter the URL/Link")
    url = st.text_input("", placeholder="e.g., https://example.com")

    # Select QR code size
    st.markdown("### 📏 Select QR Code Size")
    qr_size = st.slider("Choose QR Code Size (pixels)", min_value=100, max_value=300, value=200, step=10)

    # Generate QR Code button
    if st.button("🎨 Generate QR Code"):
        if url.strip():
            with st.spinner("Generating your QR Code..."):
                # Use an online API to generate the QR code
                qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?data={url}&size={qr_size}x{qr_size}"
                response = requests.get(qr_api_url)

                if response.status_code == 200:
                    # Convert the response content to an image
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption="🎉 Your QR Code", use_container_width=False)

                    # Add a download button for the QR Code
                    buf = BytesIO(response.content)
                    st.download_button(
                        label="📥 Download QR Code",
                        data=buf,
                        file_name="qr_code.png",
                        mime="image/png",
                    )
                else:
                    st.error("❌ Failed to generate QR Code. Please try again later.")
        else:
            st.warning("⚠️ Please enter a valid URL!")

    # Footer
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by QRServer API ✨</p>
        """,
        unsafe_allow_html=True,
    )

