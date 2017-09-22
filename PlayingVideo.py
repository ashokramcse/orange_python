# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:55:22 2017

@author: BALASUBRAMANIAM
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('dfs.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()