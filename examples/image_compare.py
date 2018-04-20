# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 18:08:10 2018

@author: blook
"""

# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
	
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
 
def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
 
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
 
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
 
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
 
    # show the images
    plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
model = cv2.imread("cercle_model.png")
carre = cv2.imread("carre_model.png")
dessin = cv2.imread("cercle_blanc.png")
 
# convert the images to grayscale
model = cv2.cvtColor(model, cv2.COLOR_BGR2GRAY)
carre = cv2.cvtColor(carre, cv2.COLOR_BGR2GRAY)
dessin = cv2.cvtColor(dessin, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Modèle", model), ("Dessin", dessin)
 
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
 
# show the figure
plt.show()
 
# compare the images
compare_images(model, model, "Modèle vs. Modèle")
compare_images(model, dessin, "Modèle vs. Dessin")
compare_images(carre, dessin, "Carré vs. Dessin")