from imutils.video import WebcamVideoStream
from imutils.video import FPS
import imutils
from threading import Thread
import cv2
import os

'''
vs = WebcamVideoStream(src=0).start()
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
count = 0
face_id = 8

while(True):

    img = vs.read()
    frame = cv2.resize(img, (150, 150))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces: 

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)     
        # Save the captured image into the datasets folder
        count += 1
        print(count)
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('camera', frame)
    
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cv2.destroyAllWindows()
vs.stop()
'''

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

cwd = os.getcwd()
print("directory", cwd)
#file=open('haarcascade_frontalface_default.xml', 'r')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_detector = cv2.CascadeClassifier(os.path.join(cwd, 'haarcascade_frontalface_default.xml'))
#face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
face_id = 8

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    print("faces:", faces)

    for (x, y, w, h) in faces: 

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        # Save the captured image into the datasets folder
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('camera', img)
        print(count)
        
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
file.close()
cam.release()
cv2.destroyAllWindows()
