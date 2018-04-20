# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:01:23 2018

@author: blook
"""

import numpy as np
import cv2

lenna = cv2.imread('lenna.png', 0)
cv2.imshow('Lenna Soderberg', lenna)
k = cv2.waitKey(0) & 0xFF
if k == 27:                 # Attend que la touche ESC soit pressée
    cv2.destroyAllWindows() # Détruit toutes les fenêtres
elif k == ord('s'):         # Attend que la touche 'S' soit pressée
    cv2.imwrite('lenna_grey.png', lenna)
    cv2.destroyAllWindows()