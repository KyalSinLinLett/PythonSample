import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1): 

	_, frame = cap.read()

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	lower_green = np.array([41, 68, 55])
	upper_green = np.array([122, 224, 185])

	lower_red = np.array([160,20,70])
	upper_red = np.array([190,255,255])

	mask_green = cv.inRange(hsv, lower_green, upper_green)
	mask_red = cv.inRange(hsv, lower_red, upper_red)

	mask = cv.bitwise_or(mask_red, mask_green)

	res = cv.bitwise_and(frame, frame, mask = mask)

	cv.imshow('frame', frame)
	cv.imshow('mask', mask)
	cv.imshow('res', res)

	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break

cv.destroyAllWindows()