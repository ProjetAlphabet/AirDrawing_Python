#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 22:14:24 2018

@author: pi
"""

import cv2
import sys


def find_car(image):

    size = cv2.GetSize(image)

    #prepare memory
    car = cv2.CreateImage(size, 8, 1)
    red = cv2.CreateImage(size, 8, 1)
    hsv = cv2.CreateImage(size, 8, 3)
    sat = cv2.CreateImage(size, 8, 1)
    
    #split image into hsv, grab the sat
    cv2.CvtColor(image, hsv, cv2.CV_BGR2HSV)
    cv2.Split(hsv, None, sat, None, None)
    
    #split image into rgb
    cv2.Split(image, None, None, red, None)
    
    #find the car by looking for red, with high saturation
    cv2.Threshold(red, red, 128, 255, cv2.CV_THRESH_BINARY)
    cv2.Threshold(sat, sat, 128, 255, cv2.CV_THRESH_BINARY)
    
    #AND the two thresholds, finding the car
    cv2.Mul(red, sat, car)
    
    #remove noise, highlighting the car
    cv2.Erode(car, car, iterations=5)
    cv2.Dilate(car, car, iterations=5)
    
    storage = cv2.CreateMemStorage(0)
    obj = cv2.FindContours(car, storage, cv2.CV_RETR_CCOMP, cv2.CV_CHAIN_APPROX_SIMPLE)
    cv2.ShowImage('A', car)
    
    if not obj:
        return(0, 0, 0, 0)
    else:
        return cv2.BoundingRect(obj)

points = []
capture = cv2.CaptureFromCAM(0)
if not capture:
    print("Error opening capture device")
    sys.exit(1)

cv2.SetCaptureProperty(capture, cv2.CV_CAP_PROP_FRAME_WIDTH, 640)
cv2.SetCaptureProperty(capture, cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)


while 1:

    original = cv2.QueryFrame(capture)
    car_rect = find_car(original)
    print(car_rect)
    middle = (car_rect[0] + (car_rect[2] / 2), car_rect[1] + (car_rect[3]/2))
    if points == []:
        points.append(middle)
    else:
        if abs(points[-1][0] - middle[0]) > 5 and abs(points[-1][1] - middle[1]) > 10:
            points.append(middle)

    cv2.Rectangle(original,
                  (car_rect[0], car_rect[1]),
                  (car_rect[0] + car_rect[2], car_rect[1] + car_rect[3]),
                  (255, 0, 0),
                  1,
                  8,
                  0)
    
    for point in points:
        cv2.Circle(original,
                   point,
                   1,
                   (0, 0, 255),
                   -1,
                   8,
                   0)

    cv2.ShowImage('Analysed', original)
    k = cv2.WaitKey(33)