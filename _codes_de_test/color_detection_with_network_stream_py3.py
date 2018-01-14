# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

import io
import socket
import struct
from PIL import Image
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 50
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(1024, 768))

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0) 

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
 
# allow the camera to warmup
time.sleep(0.1)

try:
    while True:
        
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
            image = frame.array

            blur = cv2.blur(image, (3,3))

        #hsv to complicate things, or stick with BGR
        #hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
        #thresh = cv2.inRange(hsv,np.array((0, 200, 200)), np.array((20, 255, 255)))

            lower = np.array([0,0,127],dtype="uint8")
        #upper = np.array([225,88,50], dtype="uint8")
            upper = np.array([0,0,255], dtype="uint8")

            thresh = cv2.inRange(blur, lower, upper)
            thresh2 = thresh.copy()

        # find contours in the threshold image
            image, contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        # finding contour with maximum area and store it as best_cnt
            max_area = 0
            best_cnt = 1
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > max_area:
                        max_area = area
                        best_cnt = cnt

        # finding centroids of best_cnt and draw a circle there
            M = cv2.moments(best_cnt)
            cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        #if best_cnt>1:
            cv2.circle(blur,(cx,cy),10,(0,0,255),-1)
        # show the frame
            cv2.imshow("Frame", blur)
        #cv2.imshow('thresh',thresh2)
            key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
            rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)
        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')
finally:
    connection.close()
    server_socket.close()