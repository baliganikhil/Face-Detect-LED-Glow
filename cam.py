#!/usr/bin/python

import serial
import cv

loop = True
cap = cv.CreateCameraCapture(0)
ser = serial.Serial('/dev/ttyACM1', 9600)

while loop:

    # Read image
    temp = cv.QueryFrame(cap)

    # Create another image to hold Black&White version of image
    image = cv.CreateImage((temp.width, temp.height), cv.IPL_DEPTH_8U, 1)

    # Convert original image to B/W - Only because calculations are apparently better
    cv.CvtColor(temp, image, cv.CV_BGR2GRAY)

    # Use Haar Classifier for face detection (Magic Black Box)
    storage = cv.CreateMemStorage()
    haar=cv.Load('./haarcascade_frontalface_default.xml')
    detected = cv.HaarDetectObjects(image, haar, storage, 1.2, 2,cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))

    # Returns a list, the first item of which is a tuple
    # First element of tuple is x, second is y, third and fourth are width and height
    # We pass these params to create a rectangle. If we had not converted a b/w image
    # we can have a red border around instead
    if detected:
        cv.Rectangle(image, (detected[0][0][0], detected[0][0][1]), (detected[0][0][0] + detected[0][0][2], detected[0][0][1] + detected[0][0][3]), cv.RGB(255, 0, 0), 3)
        ser.write('Just a really really long string to see something')


    # Create a named window and display image in it. Key press kills window and exits
    cv.NamedWindow('Nik')
    cv.ShowImage('Nik', image)

    char = cv.WaitKey(33)
    if (char != -1):
        if (ord(char) == 27):
            loop = False
