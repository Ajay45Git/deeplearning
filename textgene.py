import streamlit as st
import requests

# API URL and headers
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UI for Text Generation with Llama model
def llama_text_generation_page():
    # Title and introduction
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">✍️ Story Generation</h1>
            <p style="font-size: 18px; color: #555;">This app uses the <b>Llama-3.2-1B</b> model from Hugging Face to generate text based on the provided input prompt.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar Instructions
    st.write("**How to Use**")
    st.write("""
        1. Enter a prompt (starting sentence or idea).
        2. Click **Generate Text**.
        3. The app will generate a story or continuation based on your input.
    """)

    # User input for the prompt
    prompt = st.text_area("Enter your prompt here:", height=150, placeholder="Once upon a time...")

    # Generate prediction when button is clicked
    if st.button("📝 Generate Text"):
        if prompt.strip():
            with st.spinner("Generating story... Please wait."):
                try:
                    # Send the input prompt to the model
                    output = query({"inputs": prompt})

                    # Display the result
                    if output and 'generated_text' in output[0]:
                        generated_text = output[0]['generated_text']
                        st.markdown(f"**Generated Text:**\n\n{generated_text}")
                    else:
                        st.error("No output received from the model. Please try again.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid prompt!")

    # Footer credit
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by Hugging Face's Llama-3.2-1B Model ✨</p>
        """,
        unsafe_allow_html=True,
    )

