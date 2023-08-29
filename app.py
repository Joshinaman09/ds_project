import streamlit as st
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def main():
    st.title("Object Detection with Streamlit")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = cv2.imread(uploaded_file)
        bbox, label, conf = cv.detect_common_objects(image)
        output_image = draw_bbox(image, bbox, label, conf)
        st.image(output_image, caption="Detected Objects", use_column_width=True)

        for item in label:
            st.write(item)

if __name__ == "__main__":
    main()
