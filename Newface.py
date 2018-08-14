import cv2 
import Newrobot as robot
from serial import Serial
from time import sleep
from glob import glob
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera


recv=24
send=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(recv, GPIO.IN)
GPIO.setup(send, GPIO.OUT)
li=[]
li=glob("/dev/*")
port=("\n".join(s for s in li if 'ttyACM'.lower() in s.lower()))
print(port)

ser =Serial(port, 9600)
oba=0

GPIO.output(27, False)

def check():
    while 1:
##        if GPIO.input(recv):
        if 1:
            break
        else:
            sleep(1)
            robot.stopp()
            GPIO.output(send, False)

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

##cap.set(cv2.cv.CV_CAP_PROP_FPS, 60)

camera = PiCamera()
camera.resolution = (640,480)
#camera.rotation=180
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))
count=0
# allow the camera to warmup
sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#for frame in camera.capture_continuous(rawCapture, format='jpeg')
    check()

        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
    img = frame.array
    
    # reads frames from a camera
    
    
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(faces)
    if(faces==()):      
        if count>4:
            robot.rotate()
        else:
            robot.stopp()
            count+=1
        print('Stop no face')  
        GPIO.output(27, False)
    for (x,y,w,h) in faces:
        print(faces)
        count=0
        GPIO.output(27, True)
        
        # To draw a rectangle in a face 
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        if(h<85):
            try:
                ser.flushInput()
                sleep(0.01)
                obj=ser.readline()
                oba=obj[0:3]
                obv=obj[3:6]
                oba=int(oba)
                obv=int(obv)
                oba=oba-100
                obv=obv-100
            except:
                pass
            
            #oba=60
            print("obstacle at: {}".format(oba))
            print("visible at: {}".format(obv))
            
            #thoorama irruku'
            if((x<=400)and(x>=200)):
                #desti is straight but check for foreign objs
                if((oba<50)or(oba>150)):
                    #go straight
                    robot.forward(0.1)
                    
                elif(x>290):
                    robot.left(0.55)
                    sleep(0.1)
                    ser.flushInput()
                    sleep(0.01)
                    obj=ser.readline()
                    oba=obj[0:3]
                    oba=oba-100
                    if((oba<50)or(oba>150)):
                        robot.forward(2.5)
                        robot.right(0.55)
                    else:
                        robot.right(1)
                        sleep(0.1)
                        ser.flushInput()
                        sleep(0.01)
                        obj=ser.readline()
                        oba=obj[0:3]
                        oba=oba-100
                        if((oba<50)or(oba>150)):
                            robot.forward(2.5)
                            robot.left(0.55)
                elif(x<=290):
                    robot.right(0.55)
                    sleep(0.1)
                    ser.flushInput()
                    sleep(0.01)
                    obj=ser.readline()
                    oba=obj[0:3]
                    oba=oba-100
                    if((oba<50)or(oba>150)):
                        robot.forward(2.5)
                        robot.left(0.55)
                    else:
                        robot.left(1)
                        sleep(0.1)
                        ser.flushInput()
                        sleep(0.01)
                        obj=ser.readline()
                        oba=obj[0:3]
                        oba=oba-100
                        if((oba<50)or(oba>150)):
                            robot.forward(2.5)
                            robot.right(0.55)
                    
            elif(x>400):
                robot.right(0.1)
            elif(x<200):
                robot.left(0.1)
        elif(h>84):
            robot.stopp()
            GPIO.output(send, True)

            
                    


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
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    # Wait for Esc key to stop
        # if the `q` key was pressed, break from the loop
    if key == ord("q"):
       break
    
# Close the window

robot.stopp()
# De-allocate any associated memory usage
cv2.destroyAllWindows()
