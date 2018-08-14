from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import robot
from serial import Serial
from time import sleep
from glob import glob
import RPi.GPIO as GPIO

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation=180
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # To draw a rectangle in a face 
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
	
	print("x: {}".format(x))
    
	# show the frame
    cv2.imshow("Frame", img)
    key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
cv2.destroyAllWindows() 
