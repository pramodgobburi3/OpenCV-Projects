import pygame
import sys
import cv2
import numpy as np
from extractor import Extractor
	
fe = Extractor()	
def main():
	cap = cv2.VideoCapture(0)

	while True:
		_, frame = cap.read()
		process_frame(frame)
		
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break

	cv2.destroyAllWindows()
	cap.release

def process_frame(img):
	height, width, channels = img.shape
	matches = fe.extract(img)

	# for p in kps:
		# print(p)
		# u,v = map(lambda x: int(round(x)), p.pt)
		# print(u, v)
		# cv2.circle(img, (u,v), color=(0,255,0), radius=3)
		
	for pt1, pt2, in matches:
		u1,v1 = map(lambda x: int(round(x)), pt1.pt)
		u2,v2 = map(lambda x: int(round(x)), pt2.pt)
		cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
		cv2.line(img, (u1, v1), (u2, v2), color=(255,0,0))
		
	cv2.imshow('image', img)
	
if __name__ == "__main__":
	main()