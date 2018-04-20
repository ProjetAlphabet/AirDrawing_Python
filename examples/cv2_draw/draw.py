# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:06:06 2018

@author: blook
"""

import numpy as np
import cv2

# Création d'une image noire
img = np.zeros((512,512,3), np.uint8)

# Déssine un trait bleu en diagonal avec une épaisseur de 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Déssine un rectangle vert
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),-1)

# Déssine un cercle rouge dans le rectangle vert
img = cv2.circle(img,(447,63),63,(0,0,255),-1)

# Déssine une ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,360,255,-1)

# Déssine un polygone
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# Insère du texte sur l'image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)

# Enregistre l'image créée précédemment
cv2.imwrite('test.jpg', img)