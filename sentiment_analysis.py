import streamlit as st
import requests

# Function to query Hugging Face API for sentiment analysis
def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face API token
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Page function for Sentiment Analysis
def sentiment_analysis_page():
    # Title with styling
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50;">🌍 Multilingual Sentiment Analysis</h1>
            <p style="color: #555;">Analyze the sentiment of your text in multiple languages with state-of-the-art AI models.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar with instructions
    st.write("**How it Works**")
    st.write("""
        1. Enter a text in any language in the text box below.
        2. Click **Analyze** to get the sentiment of your text.
        3. The sentiment label and score will be displayed below.
    """)

    # User input for text
    st.markdown("### ✍️ Enter Text for Sentiment Analysis")
    text_input = st.text_area("Text Input", height=200, placeholder="Type your text here...")

    # Analyze button
    if st.button("🔍 Analyze Sentiment"):
        if text_input.strip():
            with st.spinner("Analyzing... 🧐"):
                try:
                    # Query Hugging Face API
                    output = query({"inputs": text_input})

                    # Check and process the response
                    if isinstance(output, list) and len(output) > 0 and isinstance(output[0], list):
                        sentiment_data = output[0]
                        sentiment = sentiment_data[0].get('label', 'No sentiment label found')
                        score = sentiment_data[0].get('score', 'No sentiment score found')

                        # Display results in a styled box
                        st.subheader("### Sentiment Analysis Result")
                        st.markdown(
                            f"""
                            <div style="background-color: #f4f8fb; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
                                <p style="font-size: 18px; color: #333;"><strong>Sentiment:</strong> {sentiment}</p>
                                <p style="font-size: 18px; color: #333;"><strong>Score:</strong> {score:.4f}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    else:
                        st.error("❌ Unexpected response format.")
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")
        else:
            st.warning("⚠️ Please enter some text to analyze!")

    # Footer with credit
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by Hugging Face's Multilingual Sentiment Model ✨</p>
        """,
        unsafe_allow_html=True,
    )

