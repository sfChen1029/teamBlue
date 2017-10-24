import cv2
import numpy as np
import math

class TargetDetector:
	#image
	#hsv_image
	def putImage(self, img):
		global image
		image = img
		global hsv_image
		hsv_image  = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	def threshold(self):
		THRESHOLD_MIN = np.array([0,0,0], np.uint8)
		THRESHOLD_MAX = np.array([250,255,220], np.uint8)
		global hsv_image
		threshed_img = cv2.inRange(hsv_image, THRESHOLD_MIN, THRESHOLD_MAX)
		return threshed_img

cv2.namedWindow("Camera Feed", cv2.WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(0)
while True:
	ret, frame = capture.read()
	targetDetector = TargetDetector()
	targetDetector.putImage(frame)
	threshed = targetDetector.threshold()
	cv2.imshow("Camera Feed", threshed)
	key = cv2.waitKey(10)
	if key == 27:
		cv2.destroyWindow("Camera Feed")
		break
