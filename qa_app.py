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
    st.title("Question Answering ")
    st.write("Provide a context and ask a question. Model will find the answer using the Hugging Face QA model.")

    # User input for context and question
    context = st.text_area("Context", "", height=200, placeholder="Enter the context here.")
    question = st.text_input("Question", "", placeholder="Enter your question here.")

    if st.button("Get Answer"):
        if context.strip() and question.strip():
            with st.spinner("Finding the answer..."):
                try:
                    # Query the model
                    output = query({"inputs": {"question": question, "context": context}})

                    # Extract the answer
                    if isinstance(output, dict):
                        answer = output.get("answer", "No answer found.")
                        st.subheader("Answer:")
                        st.write(answer)
                    else:
                        st.error("Unexpected API response format.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide both a context and a question!")
