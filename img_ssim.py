#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 23:40:20 2018

@author: cecilebecquie
"""

#importation des bibliothèques
from skimage.measure import compare_ssim as ssim   #indice de similarité structurelle
import cv2
import __var__ as glb

def compare(models, image):
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

i, sim = compare(glb.models_shap, glb.white)
image = cv2.imread(glb.models_shap[i])
mname = glb.models_shap_name

cv2.imshow(mname[i], image)
print(sim)
cv2.waitKey(0)
cv2.destroyAllWindows()