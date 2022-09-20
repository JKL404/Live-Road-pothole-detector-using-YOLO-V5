from detection import detect
import streamlit as st
from vidgear.gears import CamGear
import cv2


@st.cache(allow_output_mutation=True)
def get_cap():
    # success, frame = cv2.VideoCapture(0)
    # return cv2.VideoCapture(0)
    # return cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4')

    stream = CamGear(source='https://www.youtube.com/watch?v=THQUs18B3R0', stream_mode=True,
                     logging=True).start()  # YouTube Video URL as input
    return True, stream


def gen_frames(dtype):  # generate frame by frame from camera
    # camera = get_cap()
    success, camera = get_cap()
    frameST = st.empty()
    while True:
        # Capture frame-by-frame
        # success, frame = camera.read()  # read the camera frame using video capture
        frame = camera.read()  # read the camera frame using stream

        if not success:
            break
        else:
            frame = detect.detect_object(frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
    frameST.image(frame, channels="BGR")
