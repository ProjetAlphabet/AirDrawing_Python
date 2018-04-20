# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:38:09 2018

@author: blook
"""

# Importation de PIL
from PIL import Image
import __var__ as glb

# Conversion d'une image en noir et blanc
def convert_white(image):
    # Ouverture de l'image
    original = Image.open(glb.process)
    
    gray = original.convert('L') # Conversion de l'image ouverte en nuances de gris
    new = gray.point(lambda x: 0 if x < 80 else 255, '1') # Conversion de l'image nuances de gris en noir et blanc
    new.save(glb.white, 'png') # Enregistrement de l'image finale