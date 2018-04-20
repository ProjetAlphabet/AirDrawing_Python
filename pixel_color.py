# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:38:09 2018

@author: blook
"""
# Changement de couleur en blanc

# Importation de PIL
from PIL import Image
# Importation de OpenCV2
import cv2
import __var__ as glb

# Transforme tous les pixels autres que ceux du dessin en noir
def convert_pix():
    img = cv2.imread(glb.saved)
    y, x, z = img.shape
    
    
    # Analyse de la couleur des pixels de l'image pixel par pixel
    # Analyse de la manière suivante :
    # Pour une hauteur fixe, analyse des pixels en largeur
    # ex: ligne 0 --> anlyse du pixel colonne 0 au pixel colonne 599
    # ex: ligne 1 --> anlyse du pixel colonne 0 au pixel colonne 599
    # ex: ligne 2 --> anlyse du pixel colonne 0 au pixel colonne 599
    # etc...
    for i in range (0, y):
        for j in range (0, x):
        
            # Détection de la couleur rouge seulement (à changer pour une autre couleur si possible)
            # AIDE:
            # 0 = bleu
            # 1 = vert
            # 2 = rouge
            if (img[i, j, 0] > 10) and (img[i, j, 1] > 5) and (img[i, j, 2] < 245):
                img[i, j, 0] = 0
                img[i, j, 1] = 0
                img[i, j, 2] = 0
    
    cv2.imwrite(glb.draw, img) # Enregistrement de l'image convertie

# Conversion d'une image en noir et blanc
def convert_white():
    # Ouverture de l'image
    original = Image.open(glb.process)
    
    gray = original.convert('L') # Conversion de l'image ouverte en nuances de gris
    new = gray.point(lambda x: 0 if x < 1 else 255, '1') # Conversion de l'image nuances de gris en noir et blanc
    new.save(glb.white, 'png') # Enregistrement de l'image finale