# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py

# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2

import bounding
import pixel_color
import resizer
import __var__ as glb
import img_ssim as sim

def __init__():
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

    # if a video path was not supplied, grab the reference
    # to the webcam
    if not args.get("video", False):
        camera = cv2.VideoCapture(0)

    # otherwise, grab a reference to the video file
    else:
        camera = cv2.VideoCapture(args["video"])

    # keep looping
    while True:
        # grab the current frame
        grabbed, frame = camera.read()
        draw = np.zeros((450,600,4), np.uint8)
        
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if args.get("video") and not grabbed:
            break

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
            #thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
            thickness = 10
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

        # show the frame to our screen
        frame = cv2.flip(frame, 1) # Symétrie de la vidéo
        mask = cv2.flip(mask, 1)
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):
            print('clear')
            pts = deque(maxlen=0)
            pts = deque(maxlen=args['buffer'])
        
        if key == ord("p"):
            # Enregistrement de l'image
            cv2.imwrite(glb.cam, frame)
        
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

        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()

__init__()