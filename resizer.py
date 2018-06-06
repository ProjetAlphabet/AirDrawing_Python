#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:36:16 2018

@author: cecilebecquie
"""
# Redimension de l'image

import __var__ as glb
import cv2

def resize_image():
    # Chargement de l'image capturée
    image = cv2.imread(glb.draw)

    # Début du procédé
    dim = (512, 512) # Définition des dimensions de l'image finale
    processed = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) # Redimensionnement de l'image dans les dimensions finales
    cv2.imwrite(glb.process, processed) # Enregistrement de l'image finale