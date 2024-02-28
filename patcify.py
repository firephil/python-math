import cv2
from patchify import patchify

img = cv2.imread("black_girl.jpg")

patches = patchify(img, (3, 3), step=1)