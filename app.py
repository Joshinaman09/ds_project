import cv2
import streamlit as st
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def main():
    st.title("Real-time Object Detection with Streamlit")

    # Open the webcam
    video = cv2.VideoCapture(0)
    labels = []

    stframe = st.empty()

    while True:
        ret, frame = video.read()
        if not ret:
            break  # Break the loop if no more frames are available

        bbox, label, conf = cv.detect_common_objects(frame)

        output_image = draw_bbox(frame, bbox, label, conf)

        stframe.image(output_image, channels="BGR", caption='Real-time Object Detection')
        for item in label:
            if item in labels:
             pass
        else:
            labels.append(item)

        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Press 'q' to exit the loop

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
