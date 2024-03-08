from PIL import Image
import cv2
import os
path = '4k.png'
dim = (1024,768)

def pillow_resize(path):

    image = Image.open(path)
    return image.resize(dim, resample=Image.BICUBIC)

def opencv_resize(path):
    image = cv2.imread(path)
    return cv2.resize(image, dim)

img1 = pillow_resize(path)
img1.save("pillow.png")

img2 = opencv_resize(path)
cv2.imwrite("opecv.png",img2)



