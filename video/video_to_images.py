import cv2
import os
from moviepy.editor import *
from PIL import Image

def extractAudio(file:str):
    video = VideoFileClip(file)
    audio = video.audio
    audio.write_audiofile(file.replace(".mp4",".mp3"))

def convert_mp4_to_png(video_path):
    if not os.path.exists("images"):
        os.makedirs("images")

    cap = cv2.VideoCapture(video_path)

    count = 0
    while True:
        # Capture frame-by-frame
        success, image = cap.read()

        if not success:
            break
        if(count % 30 ==0 ):
            cv2.imwrite( "images//%06d.png" % count, image)

        count += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Get all MP4 files in the current directory
    mp4_files = [f for f in os.listdir() if f.endswith(".mp4")]

    # Convert each MP4 file to PNG images
    for mp4_file in mp4_files:
        video_path = os.path.join(os.getcwd(), mp4_file)
        extractAudio(video_path)
        convert_mp4_to_png(video_path)
