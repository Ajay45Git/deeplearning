import streamlit as st
import requests

# Hugging Face API Information
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face API key

# Function to query Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Page function for Question Answering
def qa_page():
    # Title with custom styling
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #3e8e41;">❓ Question Answering</h1>
            <p style="color: #555;">Ask a question and provide the context. The model will find the answer using state-of-the-art AI.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar instructions
    st.write("**How to Use**")
    st.write("""
        1. Enter the context (a paragraph or some information).
        2. Type your question based on the context.
        3. Press **Get Answer** to find the answer to your question.
    """)

    # User inputs for context and question
    st.markdown("### ✍️ Enter Context and Question Below:")
    context = st.text_area("Context", "", height=200, placeholder="Provide context here...")
    question = st.text_input("Question", "", placeholder="Ask a question here...")

    # Answer button
    if st.button("🔍 Get Answer"):
        if context.strip() and question.strip():
            with st.spinner("Finding the answer... 🧐"):
                try:
                    # Query the Hugging Face model
                    output = query({"inputs": {"question": question, "context": context}})

                    # Extract and display the answer
                    if isinstance(output, dict) and 'answer' in output:
                        answer = output['answer']
                        st.subheader("### Answer:")
                        st.markdown(f"<div style='padding: 15px; background-color: #f4f8fb; border-radius: 8px; border: 1px solid #ddd; color: #333;'> {answer} </div>", unsafe_allow_html=True)
                    else:
                        st.error("❌ Error: No answer found or unexpected response format.")
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")
        else:
            st.warning("⚠️ Please enter both context and question!")

    # Footer credit
    st.markdown(
        """
        <hr>
        <p style="text-align: center; color: #777;">✨ Powered by Hugging Face's Roberta QA Model ✨</p>
        """,
        unsafe_allow_html=True,
    )

