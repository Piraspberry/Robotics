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

fl=GPIO.PWM(17,100)
fr=GPIO.PWM(18,100)
rl=GPIO.PWM(22,100)
rr=GPIO.PWM(23,100)

def rotate():
        fr.start(0)
        rl.start(0)
        rr.start(50)
        fl.start(50)
        print("rotate")
        
def forward(i):
        rl.start(0)
        rr.start(0)
        fl.start(70)
        fr.start(70)
##	GPIO.output(fwdright, True)
##	GPIO.output(fwdleft, True)
##	GPIO.output(revleft, False)
##	GPIO.output(revright, False)
	print("Forward Moto")
	time.sleep(i)


def right(i):
        fr.start(0)
        rl.start(0)
        rr.start(100)
        fl.start(100)
##	GPIO.output(revright, True)
##	GPIO.output(fwdleft, True)
##	GPIO.output(revleft, False)
##	GPIO.output(fwdright, False)
        print("Right Moto")
	time.sleep(i)
	stopp()


def left(i):
        fl.start(0)
        rr.start(0)
        fr.start(100)
        rl.start(100)
##	GPIO.output(fwdright, True)
##	GPIO.output(revleft, True)
##	GPIO.output(fwdleft, False)
##	GPIO.output(revright, False)
        print("Left Moto")
	time.sleep(i)
	stopp()


def reverse(i):
        fl.start(0)
        fr.start(0)
        rl.start(50)
        rr.start(50)
##	GPIO.output(revleft, True)
##	GPIO.output(revright, True)
##	GPIO.output(fwdleft, False)
##	GPIO.output(fwdright, False)
        print("Reverse Moto")
	time.sleep(i)


def stopp():
        fl.stop()
        fr.stop()
        rl.stop()
        rr.stop()
##	GPIO.output(revleft, False)
##	GPIO.output(revright, False)
##	GPIO.output(fwdleft, False)
##	GPIO.output(fwdright, False)

	print("Stop Moto")
	#time.sleep(0.5)


try:
	print("R E A D Y")
except KeyboardInterrupt:
	print("E X I T")
	GPIO.cleanup()
