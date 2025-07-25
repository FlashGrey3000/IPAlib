# Create your own test#.py for testing
# This file is being used by flashgrey

import cv2
import numpy as np
from utils import display_on_linux
from core import invert,threshold, threshold_binary,correlate, convolution

# img = cv2.imread("assets/lucy_moon.jpg")
img = cv2.imread("assets/lucy_moon.jpg")

# img = invert(img)
# img = threshold(img, 0)
# img = threshold_binary(img, 128)
# print(len(img[0][0]))
# convolution(img, np.array([[-1,-1,-1],[-1,8,4],[-1,-1,4]]))
# img = correlate(img, np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))
# cv2.imwrite('assets/new.jpg', img)
# display_on_linux("assets/new.jpg")
# img3 = threshold(img, 198)
# cv2.imwrite('assets/new2.jpg', img3)
display_on_linux("assets/new.jpg")