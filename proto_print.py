#!/usr/bin/python
import dht
import os
import datetime

# include the library 
import RPi_I2C_driver
from time import *
import RPi.GPIO as GPIO

# RPi_I2C_driver.lcd( I2C address )
lcd = RPi_I2C_driver.lcd(0x27)

#GPIO SETUP FOR VIBRATION DETECTOR
channel = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def callback(channel):
    if GPIO.input(channel):
        print("Movement Detected!")
    else:
        print("Movement Detected!")
    
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=500)
GPIO.add_event_callback(channel, callback)

try:
    while True:
        dhtResult = dht.instance.read()
        if dhtResult.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % dhtResult.temperature)
            print("Humidity: %-3.1f %%" % dhtResult.humidity)
            
        else:
            print("fail to read DHT value. Please wait 3 secs.")

        sleep(3)
        cls()
        
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

