import cv2
import numpy as np

class VideoDevice:
	
	def feed(self):
		capture = cv2.VideoCapture(1)
		ret,frame = capture.read()
		return frame
