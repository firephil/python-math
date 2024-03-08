# python -m pip install --upgrade pip
# python -m venv image_resize_env
# image_resize_env/scripts/activate
# pip install opencv-python
# pip install pillow

import timeit
from PIL import Image
import cv2

path = '4k.jpg'
dim = (1024,768)
def pillow_resize():

    image = Image.open(path)
    return image.resize(dim, resample=Image.BICUBIC)

def opencv_resize():
    image = cv2.imread(path)
    return cv2.resize(image, dim)

num = 10
print('Pillow resize:', timeit.timeit(stmt= pillow_resize,number=num))
print('OpenCV resize:', timeit.timeit(stmt = opencv_resize, number=num))