import streamlit as st
from rembg import remove
from PIL import Image
import io


def main():
    st.title("Background Removal App")
    st.write("Upload an image to remove its background")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Display original image
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)

        # Remove background
        with st.spinner('Removing background...'):
            # Process the image
            output = remove(image)

            # Display result
            with col2:
                st.subheader("Result")
                st.image(output, use_container_width=True)

            # Convert to bytes for download
            buf = io.BytesIO()
            output.save(buf, format='PNG')
            byte_im = buf.getvalue()

            # Download button
            st.download_button(
                label="Download Result",
                data=byte_im,
                file_name="result.png",
                mime="image/png"
            )


if __name__ == "__main__":
    st.set_page_config(
        page_title="Background Removal App",
        page_icon="✂️",
        layout="wide"
    )
    main()