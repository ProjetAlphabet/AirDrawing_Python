#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 23:40:20 2018

@author: cecilebecquie
"""

# Importation des bibliothèques
from skimage.measure import compare_ssim as ssim   # Indice de similarité structurelle
import cv2
import numpy as np
import __var__ as glb

def compare(models, image, N):
    if glb.gamemode == 0:
        
        # Définition des variables
        s = np.array(np.zeros([N, 1])) # Tableau contenant les différentes valeurs de SSIM
        img = cv2.imread(image) # Ouverture de l'image à comparer via OpenCV
        m = 0 # Indice correspondant au modèle adéquat
    
        # Comparaison entre l'image et tous les modèles
        for i in range(0, N):
            for j in range(0, 1):
                model = cv2.imread(models[i]) # Chargement des modèles pour chaque i
                s[i, j] = ssim(img, model, multichannel=True) # Comparaison entre les modèles (insertion de la valeur du SSIM dans le tableau)
    
        # Définition du SSIM min à comparer
        f = s[0, 0]
    
        # Cherche le max dans le tableau contenant les SSIM
        for k in range(0, N):
            for l in range(0, 1):
                # S'il existe un max plus grand que le précédent
                if s[k, l] > f:
                    f = s[k, l] # Le max devient la valeur trouvée
                    m = k # L'indice de ce max est sauvegardé
    
    else:
         
        # Définition des variables
        s = np.array(np.zeros([N, 1])) # Tableau contenant les différentes valeurs de SSIM
        img = cv2.imread(image) # Ouverture de l'image à comparer via OpenCV
        m = 0 # Indice correspondant au modèle adéquat
    
        # Comparaison entre l'image et tous les modèles
        for i in range(0, N):
            for j in range(0, 1):
                model = cv2.imread(models[i, j]) # Chargement des modèles pour chaque i
                s[i, j] = ssim(img, model, multichannel=True) # Comparaison entre les modèles (insertion de la valeur du SSIM dans le tableau)
    
        # Définition du SSIM min à comparer
        f = s[0, 0]
    
        # Cherche le max dans le tableau contenant les SSIM
        for k in range(0, N):
            for l in range(0, 1):
                # S'il existe un max plus grand que le précédent
                if s[k, l] > f:
                    f = s[k, l] # Le max devient la valeur trouvée
                    m = k # L'indice de ce max est sauvegardé
    
    #print(s) ###DEBOGAGE###
    return m, f # Retourne l'indice et la valeur du SSIM