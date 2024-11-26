import streamlit as st
import requests

# Hugging Face API Information
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face token

# Function to query Hugging Face API for text summarization
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Page function for Text Summarization
def summarization_page():
    st.title("Text Summarization Model")
    st.write("Enter a paragraph below to summarize using the BERT-large model.")

    # User input text
    input_text = st.text_area("Input Text", height=300)

    if st.button("Summarize"):
        if input_text.strip():
            with st.spinner("Summarizing..."):
                try:
                    output = query({"inputs": input_text})
                    if isinstance(output, list) and len(output) > 0:
                        # Extract summary if response is a list
                        summary = output[0].get("summary_text", "No summary returned.")
                    elif isinstance(output, dict):
                        # Handle cases where output is a dictionary
                        summary = output.get("summary_text", "No summary returned.")
                    else:
                        summary = "Unexpected API response format."
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter text to summarize!")
