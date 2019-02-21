import cv2
from undistort import undistort

img = cv2.imread('test_imgs/test3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = undistort(img)

#Visualize distortion
cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllwindows()
