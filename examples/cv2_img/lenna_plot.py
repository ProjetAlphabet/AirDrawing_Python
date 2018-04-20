# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:21:59 2018

@author: blook
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.png', 0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()