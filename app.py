import streamlit as st
from PIL import Image
import numpy as np
from rembg import new_session, remove
import os

def main():
    st.set_page_config(
        page_title="Background Removal Web App",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    st.title("Background Removal Web App")

    # Upload image
    uploaded_image = st.file_uploader(
        "Choose an image...",
        type=["jpg", "png", "jpeg"],
        accept_multiple_files=False,
        key="file_uploader",
    )
    
    cols = st.columns(2)

    # Main content
    if uploaded_image is not None:
        original_image = Image.open(uploaded_image)
        cols[0].subheader("Original Image")
        cols[0].image(original_image, caption="Original Image", use_column_width=True)
        threshold = cols[0].slider("Background Threshold", 0, 255, value=50, step=5)

        if st.button("Remove Background"):

            input = original_image
            model_name = "isnet-general-use"
            session = new_session(model_name)
            output = remove(input, session=session)
            
            # Display and save the processed image
            cols[1].subheader("Without Background Image")
            cols[1].image(output, caption="Without Background Image", use_column_width=True)

if __name__ == "__main__":
    main()
