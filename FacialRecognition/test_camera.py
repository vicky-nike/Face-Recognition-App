from imutils.video import WebcamVideoStream
from imutils.video.pivideostream import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
import imutils
from threading import Thread
import cv2
import time

'''
vs = PiVideoStream().start()
time.sleep(1.0)

while(True):
    img = vs.read()
    frame = imutils.resize(img, width=400)
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1) & 0xFF

print("\n [INFO] Exiting Program and cleanup stuff")
cv2.destroyAllWindows()
vs.stop()
'''

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(320, 240))
stream = camera.capture_continuous(rawCapture, format="bgr",
	use_video_port=True)

time.sleep(2.0)

for (i, f) in enumerate(stream):
    frame = f.array
    frame = imutils.resize(frame, width=400)
    cv2.imshow('camera', frame)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)

cv2.destroyAllWindows()
stream.close()
rawCapture.close()
camera.close()