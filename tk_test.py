# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:20:20 2018

@author: blook
"""

import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from collections import deque
import argparse
import imutils

import bounding
import pixel_color
import resizer
import __var__ as glb
import img_ssim as sim

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=2048,
                help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args['buffer'])
camera = cv2.VideoCapture(0)

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    global pts, camera
    
    # grab the current frame
    grabbed, frame = camera.read()
    
    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
        
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    # update the points queue
    pts.appendleft(center)

    # loop over the set of tracked points
    for i in range(1, len(pts)):
        # if either of the tracked points are None, ignore
        # them
        if pts[i - 1] is None or pts[i] is None:
            continue

        # otherwise, compute the thickness of the line and
        # draw the connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    # show the frame to our screen
    frame = cv2.flip(frame, 1) # Symétrie de la vidéo
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    return(frame)

def key_clear(e):
    global pts
    
    pts = deque(maxlen=0)
    pts = deque(maxlen=args['buffer'])
    print('clear')
        
def key_print(e):
    global pts
    
    # Enregistrement de l'image
    cv2.imwrite(glb.cam, show_frame())
        
    # Effacement du tracé
    pts = deque(maxlen=0)
    pts = deque(maxlen=args['buffer'])
        
    # Traitement de l'image
    bounding.processing() # Récupération du tracé seul
    pixel_color.convert_pix() # Conversion des pixels autres que ceux du tracé en noir
    resizer.resize_image() # Redimensionnement de l'image en 512x512
    pixel_color.convert_white() # Conversion des pixels du tracé en blanc
    
    sim.compare(glb.models_shap, glb.white)
    indic, sim_compare = sim.compare(glb.models_shap, glb.white)
    image_compare = cv2.imread(glb.models_shap[indic])
    mname = glb.models_shap_name

    cv2.imshow(mname[indic], image_compare)
    print(sim_compare)
    cv2.waitKey(0)
    cv2.destroyWindow(mname[indic])

#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)
sliderFrame.bind("<Delete>", key_clear)
sliderFrame.bind("<Return>", key_print)
sliderFrame.focus_set()

show_frame()  #Display 2
window.mainloop()  #Starts GUI
camera.release()