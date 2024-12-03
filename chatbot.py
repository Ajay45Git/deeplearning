import streamlit as st
import requests

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face API key


# Function to query the Hugging Face API
def query_huggingface(model, messages, max_tokens=500):
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return None


# Page function for chatbot
def chatbot_page():
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

    # Title and instructions with enhanced styling
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #4CAF50; font-size: 2.5em; font-family: 'Arial', sans-serif;">🤖 AI Chatbot</h1>
            <p style="color: #555; font-size: 1.2em;">Chat with the <b>Qwen2.5-Coder-32B-Instruct</b> model powered by Hugging Face.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Handle user input and update the chat
    def handle_input():
        user_input = st.session_state.user_input
        if user_input.strip():  # Check for non-empty input
            st.session_state["messages"].append({"role": "user", "content": user_input})

            # Query the Hugging Face API for a response
            try:
                response = query_huggingface(
                    model="Qwen/Qwen2.5-Coder-32B-Instruct",
                    messages=st.session_state["messages"]
                )
                if response:
                    reply = response["choices"][0]["message"]["content"]
                    st.session_state["messages"].append({"role": "assistant", "content": reply})
            except Exception as e:
                st.session_state["messages"].append(
                    {"role": "assistant", "content": f"An error occurred: {e}"}
                )

            # Clear the input box after processing
            st.session_state.user_input = ""

    # "New Chat" button with custom styling
    if st.button("📝 New Chat", use_container_width=True):
        st.session_state["messages"] = []
        st.success("Started a new chat!", icon="✅")

    # Chat history display with alternating color for user and assistant
    st.markdown("### Chat History", unsafe_allow_html=True)
    for idx, msg in enumerate(st.session_state["messages"]):
        if msg["role"] == "user":
            st.markdown(f"<div style='background-color: #f1f1f1; padding: 10px; border-radius: 5px; margin-bottom: 10px;'><b>You: </b> {msg['content']}</div>", unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f"<div style='background-color: #e8f4e8; padding: 10px; border-radius: 5px; margin-bottom: 10px;'><b>AI: </b> {msg['content']}</div>", unsafe_allow_html=True)

    # Input box for user message with focus on user experience
    st.text_input(
        "You:",
        value=st.session_state.user_input,
        placeholder="Type your message here and press Enter...",
        key="user_input",
        on_change=handle_input,
        max_chars=500,
        label_visibility="collapsed",
        help="Ask me anything!",
        )

# Uncomment this line to run the page:
# chatbot_page()
