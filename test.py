# Create your own test#.py for testing
# This file is being used by flashgrey

import cv2
from utils import display_on_linux
from core import invert,threshold, threshold_binary

img = cv2.imread("assets/lucy_moon.jpg")

# img = invert(img)
# img = threshold(img, 198)
img2 = threshold_binary(img, 198)

cv2.imwrite('assets/new.jpg', img2)

display_on_linux("assets/new.jpg")
img3 = threshold(img, 198)
cv2.imwrite('assets/new2.jpg', img3)
display_on_linux("assets/new2.jpg")