# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:12:23 2018

@author: blook
"""

import cv2

im = cv2.imread('./ressources/ball-tracking/test.jpg')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
_, contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    roi=im[y:y+h,x:x+w]
    cv2.imwrite(str(idx) + '.jpg', roi)
    cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)
cv2.imshow('img',im)
cv2.waitKey(0)   