# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:31:22 2018

@author: blook
"""

import numpy as np
import cv2

# Mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Création d'une image noire, d'une fenêtre et associe la fonction à la fenêtre
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Draw with mouse')
cv2.setMouseCallback('Draw with mouse', draw_circle)

while(1):
    cv2.imshow('Draw with mouse', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()