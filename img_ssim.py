#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 23:40:20 2018

@author: cecilebecquie
"""

#importation des bibliothèques
from skimage.measure import compare_ssim as ssim   #indice de similarité structurelle
import cv2
import numpy as np
import __var__ as glb

def compare(models, image, N, M):
    
    if glb.gamemode == 0:
        s = []
        img = cv2.imread(image)
        j = 0
        for i in range(0, len(models)):
            model = cv2.imread(models[i])
            s.append(ssim(img, model, multichannel=True))
        f = s[0]
        for k in range(1, len(s)):
            if s[k] > f:
                f = s[k]
                j = k
        return j, f
    
    else:
        s = []
        somme = 0
        img = cv2.imread(image)
        m = 0
        for i in range(0, N):
            for j in range(0, M):
                model = cv2.imread(models[i, j])
                somme = somme + ssim(img, model, multichannel=True)
            s.append(somme)
            somme = 0
        f = s[0]
        for k in range(0, len(s)):
            if s[k] > f:
                f = s[k]
                m = k
        print(s)
        return m, f