import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#hsv hue sat value
	lower_red = np.array([0,0,0])
	upper_red = np.array([255, 255, 255])
	
	mask = cv2.inRange(hsv, lower_red, upper_red)
	result = cv2.bitwise_and(frame, frame, mask=mask)
	
	boundaries = [
		([17, 15, 100], [50, 56, 200]),
		([86, 31, 4], [220, 88, 50]),
		([25, 146, 190], [62, 174, 250]),
		([103, 86, 65], [145, 133, 128]),
	]
	
	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(frame, lower, upper)
		output = cv2.bitwise_and(frame, frame, mask = mask)

		# show the images
		cv2.imshow("images", np.hstack([frame, output]))

	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', result)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	
cv2.destroyAllWindows()
cap.release