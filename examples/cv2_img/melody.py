# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:57:50 2018

@author: blook
"""

import numpy as np
import cv2

# Charge une image en nuances de gris
img_grey = cv2.imread('melody.jpg', 0)
img_color = cv2.imread('melody.jpg', 1)
img_unchanged = cv2.imread('melody.jpg', -1)

"""
######################################################
Etape 1: affichage d'une image dans une fenêtre simple
######################################################
"""

# Affichage de l'image chargée
cv2.imshow('Dimitri Vegas, Like Mike, Steve Aoki, Ummet Ozcan - Melody (Extended Mix)', img_grey) # ARG = ('Titre de la fenêtre', image à afficher)
cv2.waitKey(0) # Attend qu'une touche du clavier soit pressée pour continuer le programme // ARG = (temps en ms)
cv2.destroyAllWindows() # Détruit toutes les fenêtres relatives à OpenCV et termine le programme

#cv2.destroyWindow() # Détruit une fenêtre spécifique // ARG = ('nom de la fenêtre')

"""
######################################################
Etape 2: affichage d'une image dans une fenêtre redimensionnable
######################################################
"""

# Affichage de l'image chargée
cv2.namedWindow('Dimitri Vegas, Like Mike, Steve Aoki, Ummet Ozcan - Melody (Extended Mix)', cv2.WINDOW_NORMAL)
cv2.imshow('Dimitri Vegas, Like Mike, Steve Aoki, Ummet Ozcan - Melody (Extended Mix)', img_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
######################################################
Etape 3: écrire une image
######################################################
"""

# Ecriture d'une image en nuance de gris, en couleur et en inchangé
cv2.imwrite('melody_grey.jpg', img_grey)
cv2.imwrite('melody_color.jpg', img_color)
cv2.imwrite('melody_unchanged.jpg', img_unchanged)