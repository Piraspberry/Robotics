import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

fwdleft = 17
fwdright = 18

revleft = 22
revright = 23

motors = [fwdleft,fwdright,revleft,revright]

for item in motors:
	GPIO.setup(item, GPIO.OUT)

def forward(i):
	GPIO.output(fwdright, True)
	GPIO.output(fwdleft, True)
	GPIO.output(revleft, False)
	GPIO.output(revright, False)
	print("Forward Moto")
	#time.sleep(i)
	#GPIO.output(fwdright, False)
	#GPIO.output(fwdleft, False)

def right(i):
	GPIO.output(revright, True)
	GPIO.output(fwdleft, True)
	GPIO.output(revleft, False)
	GPIO.output(fwdright, False)
        print("Right Moto")
	#time.sleep(i)
	#GPIO.output(revright, False)
	#GPIO.output(fwdleft, False)	

def left(i):
	GPIO.output(fwdright, True)
	GPIO.output(revleft, True)
	GPIO.output(fwdleft, False)
	GPIO.output(revright, False)
        print("Left Moto")
	#time.sleep(i)
	#GPIO.output(fwdright, False)
	#GPIO.output(revleft, False)

def reverse(i):
	GPIO.output(revleft, True)
	GPIO.output(revright, True)
	GPIO.output(fwdleft, False)
	GPIO.output(fwdright, False)
        print("Reverse Moto")
	#time.sleep(i)
	#GPIO.output(revleft, False)
	#GPIO.output(revright, False)

def stopp():
	GPIO.output(revleft, False)
	GPIO.output(revright, False)
	GPIO.output(fwdleft, False)
	GPIO.output(fwdright, False)
	#time.sleep(0.3)
	print("Stop Moto")
	#GPIO.output(revleft, False)
	#GPIO.output(revright, False)

try:
	print("R E A D Y")
except KeyboardInterrupt:
	print("E X I T")
	GPIO.cleanup()
