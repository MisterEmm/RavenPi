import os, random
from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False)

myGPIO=18
 
myCorrection=0.45
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

def rndcaw ():
    randomfile = random.choice(os.listdir("/home/pi/Music"))
    file = ' /home/pi/Music/'+ randomfile
    print(file)
    os.system ('omxplayer -o local' + file)

GPIO.output(15,True)



servo.mid()
print("mid")
sleep(0.5)
servo.min()
print("min")

rndcaw ()

sleep(1)
servo.mid()
print("mid")
sleep(0.5)
servo.max()
print("max")

rndcaw ()

sleep(1)

sleep(1)
servo.mid()
print("mid")

sleep(1)
GPIO.output(15,False)
sleep(1)

