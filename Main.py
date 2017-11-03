import cv2
from VideoDevice import VideoDevice
from TargetDetector import TargetDetector
from TargetProcessor import TargetProcessor

cv2.namedWindow("Camera Feed", cv2.WINDOW_AUTOSIZE)
video = VideoDevice()
while True:
        #get image from camera
        frame = video.feed()
        #initialize targetDetector and targetProcessor
        targetDetector = TargetDetector()
        targetProcessor = TargetProcessor()

        #threshold
        targetDetector.putImage(frame)
        threshed = targetDetector.threshold()

        #contour
        targetProcessor.putThreshed(threshed,frame)
        contour = targetProcessor.contour()

        cv2.drawContours(frame, contour, -1, (10,255,255), 5)
        #cv2.imshow("Camera Feed", frame)
        targetProcessor.calculateData()
        key = cv2.waitKey(10)
        if key == 27:
                cv2.destroyWindow("Camera Feed")
                break
