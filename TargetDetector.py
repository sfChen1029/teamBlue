import cv2
import numpy as np
import math

class TargetDetector:
	image = ""
	hsv_image = ""
	def putImage(img):
		image = img
		hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	def threshold():
		THRESHOLD_MIN = np.array([150,240,95], np.uint8)
 		THRESHOLD_MAX = np.array([250,255,220], np.uint8)
		threshed_img = cv2.inRange(orig_img, THRESHOLD_MIN, THRESHOLD_MAX)
		return threshed_img

cv2.namedWindow("Camera Feed", cv2.CV_WINDOW_AUTOSIZE)
capture = cv2.VideoCapture(0)
While True:
	ret,frame = capture.read()
	targetDetector = TargetDetector()
	targetDetector.putImage(frame)
	threshed = targetDetector.threshold()
	cv2.ShowImage("Camera Feed", threshed)
	key = cv2.waitKey(10)
	if key == 27:
		cv2.destroyWindow("Camera Feed")
		break