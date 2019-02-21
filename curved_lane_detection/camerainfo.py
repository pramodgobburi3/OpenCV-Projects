import cv2
import sys

cap = cv2.VideoCapture(0)
print(dir(cap))
while True:
    ret, frame = cap.read()
    print(frame.shape)
    
    k = cv2.waitKey(5) * 0xFF
    if k ==27:
        break
cap.release()
