import streamlit as st
from imagetotext import image_to_text_page
from imageclassification import image_classification_page  # Assuming you have a module for image classification

def main():
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Image Classification", "Image to Text"])

    # Load the appropriate page based on sidebar selection
    if page == "Image Classification":
        image_classification_page()
    elif page == "Image to Text":
        image_to_text_page()

if __name__ == "__main__":
    main()
