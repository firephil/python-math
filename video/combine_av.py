# Combine Video and Audio streams

import os
from moviepy.editor import *

video = VideoFileClip("1.mp4")
audioclip = AudioFileClip("audio.mp3")
new_audioclip = CompositeAudioClip([audioclip])
video.audio = new_audioclip
video.write_videofile('out.mp4', fps=30)