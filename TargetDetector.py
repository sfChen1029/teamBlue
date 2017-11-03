import cv2
import numpy as np
import math
from TargetProcessor import TargetProcessor

class TargetDetector:
	#image
	#hsv_image
	def putImage(self, img):
		global image
		image = img
		global hsv_image
		hsv_image  = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	def threshold(self):
		THRESHOLD_MIN = np.array([50,0,0], np.uint8)
		THRESHOLD_MAX = np.array([60,50,255], np.uint8)
		global hsv_image
		threshed_img = cv2.inRange(hsv_image, THRESHOLD_MIN, THRESHOLD_MAX)
		return threshed_img
