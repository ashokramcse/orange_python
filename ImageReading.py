# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:33:23 2017

@author: BALASUBRAMANIAM
"""

import cv2
print(cv2.__version__)

import numpy as np

# Load an color image in grayscale
img = cv2.imread('admk.jpg',0)
#Display an image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite('symbolgray.png',img)
cv2.destroyAllWindows()
