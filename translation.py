import streamlit as st
import requests

# Hugging Face API Information
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"
headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token

# Function to query Hugging Face API for translation
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Page function for Language Translation
def translation_page():
    # Title and introduction
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">🌍 Language Translator 🌎</h1>
            <p style="color: #555;">Translate text from various languages to English using cutting-edge AI models.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar instructions
    st.write("**Instructions**")
    st.write("""
        1. Enter text in the box below.
        2. Click **Translate** to see the translation.
        3. The translated text will appear below the button.
    """)

    # Input text area for the user to enter the text to translate
    st.markdown("### ✍️ Input Text")
    text_to_translate = st.text_area(
        "",
        placeholder="Enter the text you want to translate...",
        height=200
    )

    # Translate button
    if st.button("🌟 Translate"):
        if text_to_translate.strip():
            with st.spinner("Translating... 🌐"):
                try:
                    # Query the model for translation
                    output = query({"inputs": text_to_translate})

                    # Check if the response contains the expected data
                    if isinstance(output, list) and len(output) > 0 and "translation_text" in output[0]:
                        translation = output[0]["translation_text"]
                        st.markdown("### 🎯 Translated Text")
                        st.markdown(
                            f"""
                            <div style="background-color: #f4f8fb; padding: 15px; border-radius: 5px; border: 1px solid #ddd;">
                                <p style="font-size: 16px; color: #333;">{translation}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.error("Unexpected response format. Please try again.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("⚠️ Please enter some text to translate!")

    # Footer
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">Powered by Hugging Face API 🚀</p>
        """,
        unsafe_allow_html=True,
    )
