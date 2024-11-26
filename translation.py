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
    st.title("Language Translation")
    st.write("Translate text from one language to English using Hugging Face translation models.")

    # Input text area for the user to enter the text to translate
    text_to_translate = st.text_area("Enter text to translate", "", height=200, placeholder="Enter text here.")

    if st.button("Translate"):
        if text_to_translate.strip():
            with st.spinner("Translating..."):
                try:
                    # Query the model for translation
                    output = query({"inputs": text_to_translate})

                    # Check if the response contains the expected data
                    if isinstance(output, list) and len(output) > 0 and "translation_text" in output[0]:
                        translation = output[0]["translation_text"]
                        st.subheader("Translated Text:")
                        st.write(translation)
                    else:
                        st.error("Unexpected response format.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter some text to translate!")
