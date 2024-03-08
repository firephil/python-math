from moviepy.editor import *

video = VideoFileClip("video.mp4") 
audio = video.audio
audio.write_audiofile("audio.mp3")