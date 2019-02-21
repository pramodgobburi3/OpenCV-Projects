import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('images/'+str(sys.argv[1]))
    img = cv2.resize(img, (1080, 720))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thres = cv2.threshold(gray, 127, 255, 0)
    img2, contours, hierarchy = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours_img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

    canny_img = cv2.Canny(gray, 100, 200, 3)
   
    cv2.imshow('gray',gray)
    cv2.imshow('canny', canny_img)
    cv2.imshow('contours', contours_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
