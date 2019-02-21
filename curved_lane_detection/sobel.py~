import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1) 
    sobelmist = cv2.Sobel(frame, cv2.CV_32F, 1, 1)
    sobelmist64 = cv2.Sobel(frame, cv2.CV_64F, 1, 1)
    abs_sobelx = np.absolute(sobelmist64)
    scaled_sobel = np.uint8(266*abs_sobelx/np.max(abs_sobelx))
    
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('sobelmyst32', sobelmist)
    cv2.imshow('sobelmyst64', sobelmist64)
    cv2.imshow('sobelmyst64abs', abs_sobelx)
    cv2.imshow('scaled_sobel', scaled_sobel)
    

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
