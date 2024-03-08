#https://github.com/libvips/pyvips
# opencv
# pillow

import timeit
from PIL import Image
#from pyvips import Image as vips
import cv2
import os

# add vips image library to the path
vipshome = 'c://vips-dev-8.15//bin'
os.environ['PATH'] = vipshome + ';' + os.environ['PATH']

path = 'C://Users//phili//OneDrive//Υπολογιστής//1//1.png'

def pillow_resize():
    image = Image.open(path)
    return image.resize((600, 400), resample=Image.NEAREST)

def opencv_resize():
    image = cv2.imread(path)
    return cv2.resize(image, (600, 400))

def pyvips_resize():
    #im = vips.open(path)
    #return im.resize((600, 400))
    pass

num = 100
print('Pillow resize:', timeit.timeit(stmt= pillow_resize,number=num))
#print('Pysct resize:', timeit.timeit(setup pyvips_resize, number=num))
print('OpenCV resize:', timeit.timeit(stmt = opencv_resize, number=num))