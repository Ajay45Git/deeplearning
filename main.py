import requests
from streamlit_lottie import st_lottie  # Import for animation
from streamlit import sidebar, error, title, write
from streamlit_option_menu import option_menu
from imagetotext import image_to_text_page
from imageclassification import image_classification_page
from texttoimage import text_to_image_page
from chatbot import chatbot_page
from object_detection import object_detection_page
from qa_app import qa_page
from sentiment_analysis import sentiment_analysis_page
from summarization import summarization_page
from textgene import llama_text_generation_page
from translation import translation_page
from word_cloud import wordcloud_page
from qr import qr_code_generator_page  # Import the QR Code Generator


# Function to load Lottie animation from URL
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for successful request
        return r.json()  # Return the animation JSON
    except requests.exceptions.RequestException as e:
        error(f"Error loading animation: {e}")
        return None


def main():
    # Sidebar for navigation
    with sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # Sidebar Title
            options=[
                "Home", "Image Classification", "Image to Text", "Text to Image","Word Cloud","Story Generation",
                "AI Chatbot", "Object Detection", "Question Answering",
                "Sentiment Analysis", "Text Summarization", "Language Translation",
                "QR Code Generator",
                "About", "Contact"
            ],
            icons=[
                "house", "file-earmark-image", "file-earmark-text", "image","cloud", "book",
                "chat-left-text", "camera-video", "question-circle",
                "chat-left-dots", "newspaper", "translate", "qr code",
                "info-circle", "envelope"
            ],
            menu_icon="cast",  # Icon for the sidebar menu
            default_index=0,
            styles={
                "container": {"padding": "8px", "background-color": "#f0f4f8", "border-radius": "8px"},
                # Reduced padding
                "icon": {"color": "#4CAF50", "font-size": "18px"},  # Reduced font size for icons
                "nav-link": {"font-size": "14px", "margin": "6px 0", "padding": "8px", "color": "#333",
                             "font-weight": "bold"},  # Reduced font size and margin
                "nav-link-selected": {"background-color": "#4CAF50", "color": "white", "font-size": "16px",
                                      "font-weight": "bold"},  # Adjusted selected item size
                "nav-link-hover": {"background-color": "#ddd", "color": "#333"},
            }
        )

    # Home section with animated welcome message
    if selected == "Home":
        title("Welcome to Our AI-powered Platform!")

        # Add animated Lottie animation for an interactive feel
        animation = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_khzniaya.json")

        if animation:
            st_lottie(animation, speed=1, width=500, height=300, key="welcome_animation")

        # Attractive welcome message
        write("""
                    👋 **Welcome to our platform!**  
                    Dive into a world of cutting-edge AI models and tools designed to perform a wide range of tasks.  
                    Whether you need **image classification**, **text summarization**, **question answering**, or much more —  
                    we have you covered with our user-friendly AI-powered services.

                    **To get started, simply click on the options in the sidebar (top left corner) to access the AI tools.**  
                    
                    Explore the features and start interacting with the tools today!  
                    Let's make AI easy and fun! 🚀
                """)

    # Other sections
    elif selected == "Image Classification":
        image_classification_page()
    elif selected == "Image to Text":
        image_to_text_page()
    elif selected == "Text to Image":
        text_to_image_page()
    elif selected == "Word Cloud":
        wordcloud_page()
    elif selected == "Story Generation":
        llama_text_generation_page()
    elif selected == "AI Chatbot":
        chatbot_page()
    elif selected == "Object Detection":
        object_detection_page()
    elif selected == "Question Answering":
        qa_page()
    elif selected == "Sentiment Analysis":
        sentiment_analysis_page()
    elif selected == "Text Summarization":
        summarization_page()
    elif selected == "Language Translation":
        translation_page()
    elif selected == "QR Code Generator":
        qr_code_generator_page()  # Call the QR Code Generator function
    elif selected == "About":
        title("About Us")
        write("""
            Welcome to our platform! We specialize in providing AI-powered tools for a variety of tasks, including **image classification**, **text summarization**, **sentiment analysis**, and more. 
            Our models are sourced from Hugging Face's pre-trained models, ensuring high performance and reliability. 

            Whether you are a developer looking for powerful APIs, a researcher in need of advanced models, or someone exploring AI tools, we strive to make cutting-edge technology accessible to everyone. 

            Our goal is to simplify the use of artificial intelligence and make it easy to integrate into real-world applications. Start exploring today and unlock the power of AI!
            """)
    elif selected == "Contact":
        title("Contact Us")
        write("""
        We’re here to assist you! Whether you have questions, feedback, or need support, feel free to reach out to us:

        - **Email**: [Ajay Saroj](mailto:ajay45saroj@gmail.com)
        - **LinkedIn**: [Ajay Saroj](https://www.linkedin.com/in/ajay-kumar-saroj-8b5b50280?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)


        Our team is always ready to help you with any inquiries or concerns. Don't hesitate to get in touch — we value your feedback!
        """)


if __name__ == "__main__":
    main()
