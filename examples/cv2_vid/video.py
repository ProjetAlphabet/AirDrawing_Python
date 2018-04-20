# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:53:46 2018

@author: blook
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    # Capturer image par image
    ret, frame = cap.read()
    
    if ret == True:    
        # Affichage de la capture vidéo en nuances de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Afficher la capture résultante
        cv2.imshow('cv2_vid', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('test.jpg', gray)
    else:
        break
        
# Quand tout est fini, arrêter la capture
cap.release()
out.release()
cv2.destroyAllWindows()