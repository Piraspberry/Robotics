import cv2 
import robot
from serial import Serial
from time import sleep
from glob import glob
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
li=[]
li=glob("/dev/*")
port=("\n".join(s for s in li if 'ttyACM'.lower() in s.lower()))
print(port)

ser =Serial(port, 9600)
oba=0

GPIO.output(27, False)

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# 
# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_eye.xml
# Trained XML file for detecting eyes
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
 
# capture frames from a camera
cap = cv2.VideoCapture(0)
##cap.set(cv2.cv.CV_CAP_PROP_FPS, 60)
# loop runs if capturing has been initialized.
count=6
while 1:
    
    # reads frames from a camera
    
    while(count<7):                                                                                    
        ret, img = cap.read() 
        count+=1
    count=6
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    if(faces==()):      
        robot.stopp()
        print('Stop no face')  
 	GPIO.output(27, False)
    GPIO.output(27, False)
    for (x,y,w,h) in faces:
	GPIO.output(27, True)
	
        # To draw a rectangle in a face 
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if(h<180):
            ser.flushInput()
            sleep(0.01)
            oba=ser.readline()
            print("oba: {}".format(oba))
            #thoorama irruku'
            if((x<=300)and(x>=200)):
                #desti is straight but check for foreign objs
                if((oba<70)or(oba>110)):
                    #go straight
                    robot.forward(0.5)
                elif(x>255):
                    robot.left(0.5)
                elif(x<=255):
                    robot.right(0.5)
            elif(x>300):
                robot.right(0.5)
            elif(x<200):
                robot.left(0.5)
        elif(h>180):
            robot.stopp()

            
                    


##      eyes = eye_cascade.detectMultiScale(roi_gray) 
## 	print('x:{}'.format(x))

##	if(x==0):
##		robot.stopp()
##	elif(x<200):
##		print('Go {} to left'.format(int(255-x)))
##		robot.left(0.5)
##
##
##	elif(x>300):
##		print('Go {} to right'.format(int(x-255)))
##        	robot.right(0.5)
##	elif(200<x<300):
##		print('Stopp')
##		robot.stopp()
##	else:
##		pass
##        if(h<150):
##		print('forward')
##		robot.reverse(0.75)
##	else:	
##		print('for stop')
##        	robot.stopp()
##
##	print('_____________')
##        #To draw a rectangle in eyes
##        #for (ex,ey,ew,eh) in eyes:
##            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
##        print('outside if ard')
##    	if(ser.readline()=='s'):
##		robot.stopp()
##		print('inside if ard')
##	else:
##		pass
##		print('inside else ard')
    # Display an image in a window
    cv2.imshow('img',img)
 
    # Wait for Esc key to stop
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

# Close the window
cap.release()
robot.stopp()
# De-allocate any associated memory usage
cv2.destroyAllWindows() 
