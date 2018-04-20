# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 22:20:30 2018

@author: blook
"""

from skimage.measure import compare_ssim as ssim
import cv2

imageA = cv2.imread("cercle_blanc.png")
imageB = cv2.imread("carre_blanc.png")
name = ["Cercle", "Carre"]
models = ["cercle_model.png", "carre_model.png"]

def compare(imageA, models):
    sim = []
    j = 0
    for i in range(0, len(models)):
        model = cv2.imread(models[i])
        sim.append(ssim(imageA, model, multichannel=True))
        model = []
    comp = sim[0]
    for k in range(1, len(sim)):
        if sim[k] > comp:
            comp = sim[k]
            j = k
    return j

### CARRE BLANC ###
carre = cv2.imread(models[compare(imageB, models)])
cv2.imshow(name[compare(imageB, models)], carre)
print(name[1])
cv2.waitKey(0)
cv2.destroyAllWindows()

### CERCLE BLANC ###
cercle = cv2.imread(models[compare(imageA, models)])
cv2.imshow(name[compare(imageA, models)], cercle)
print(name[0])
cv2.waitKey(0)
cv2.destroyAllWindows()