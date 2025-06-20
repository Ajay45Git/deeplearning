
import streamlit as st
from PIL import Image
import io
import requests

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/detr-resnet-50"
HEADERS = {
    "Authorization": f"Bearer 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",
    "Content-Type": "image/jpeg"
}

def detect_objects(image_bytes):
    response = requests.post(API_URL, headers=HEADERS, data=image_bytes)
    if response.status_code == 200:
        return response.json()
    return None

def object_detection_page():
    st.title("Object Detection")

    file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if file:
        image = Image.open(file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Detect Objects"):
            with st.spinner("Detecting..."):
                buf = io.BytesIO()
                image.save(buf, format="JPEG")
                result = detect_objects(buf.getvalue())

            if result:
                st.subheader("Detected Objects:")
                for obj in result:
                    st.write(f"{obj['label'].capitalize()} - {obj['score']:.2%}")
            else:
                st.error("No objects detected or error in API.")
