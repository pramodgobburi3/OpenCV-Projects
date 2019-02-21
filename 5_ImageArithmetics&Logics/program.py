import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

#Simple binary addition of two images
add = img1 + img2

#CV addition method = adds the color values of each individual pixels, if the color values are greater than 255 they are rounded to 255
cvadd = cv2.add(img1, img2)

#Adding images using "weight" (set transparency to images)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

#Overlaying img3 (python logo) on img1
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

#Mask of the logo and create inverse mask
img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

ret, mask =cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

#Blacks out the area of the python logo in the first image (ROI)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

#Extract the region of the python logo from python image
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()