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
    # Title and intro with styling
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">📝 Text Summarizer 🚀</h1>
            <p style="color: #555;">Quickly summarize any paragraph using AI-powered models.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar with instructions
    st.write("**How it Works**")
    st.write("""
        1. Enter a paragraph or text in the box below.
        2. Click **Summarize** to generate a concise summary.
        3. The summary will appear right after the button.
    """)

    # User input text
    st.markdown("### ✍️ Enter Your Text Here")
    input_text = st.text_area("Input Text", height=300, placeholder="Paste your text here...")

    # Summarize button
    if st.button("🚀 Summarize"):
        if input_text.strip():
            with st.spinner("Summarizing... 🔍"):
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
                    st.subheader("### 📝 Summary:")
                    st.markdown(f"<div style='background-color: #f4f8fb; padding: 20px; border-radius: 5px; border: 1px solid #ddd;'><p style='font-size: 16px; color: #333;'>{summary}</p></div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")
        else:
            st.warning("⚠️ Please enter text to summarize!")

    # Footer with credits
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by Hugging Face API ✨</p>
        """,
        unsafe_allow_html=True,
    )

