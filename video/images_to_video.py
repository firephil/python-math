# pip install imageio-ffmpeg
import imageio
import glob
import os

writer = imageio.get_writer('1.mp4', fps=30)

print(os.getcwd())

for file in os.listdir(os.curdir):
    if (file.endswith(".png")):
        print(file)
        im = imageio.v3.imread(file)
        writer.append_data(im)
writer.close()