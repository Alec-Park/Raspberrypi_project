#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

status = False

def callback(channel):
    if GPIO.input(channel):
        status = True
        print("Movement Detected!")
        print("%d", status)
    else:
        status = True
        print("Movement Detected!!!!!")
        print("%d", status)
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=500) # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback) # assign function to GPIO PIN, Run function on change

#while True:
#    time.sleep(1)
            
