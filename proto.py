#!/usr/bin/python
import dht
#import vibrator

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

def callback(channel):
    if GPIO.input(channel):
        lcd.setCursor(0, 1)
        lcd.print("VIBRATION")
        sleep(1)
        lcd.setCursor(0, 1)
        lcd.print("                ")
    else:
        lcd.setCursor(0, 1)
        lcd.print("VIBRATION")
        sleep(1)
        lcd.setCursor(0, 1)
        lcd.print("                ")
	
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=500)
GPIO.add_event_callback(channel, callback)

# Turn on the cursor:
#lcd.cursor()

# Print a message to the LCD.
#lcd.print("Hello")

#sleep(1)

# At 0.5c second interval " World!!!" Print
#lcd.print(" World!!!", 0.5)

#print("Last valid input: " + str(datetime.datetime.now()))
#print("Temperature: %-3.1f C" % result.temperature)
#print("Humidity: %-3.1f %%" % result.humidity)
#lcd.print("Temperature: ")
#lcd.print("Humidity: ")

#sleep(2)

#lcd.clear()

# Turn off the cursor:
#lcd.noCursor()

temperature = 0
humidity = 0
vibrationDetected = False

lcd.clear()

try:
    while True:
	    dhtResult = dht.instance.read()
	    if dhtResult.is_valid():
	        temperature = dhtResult.temperature
	        humidity = dhtResult.humidity
		
	    lcd.setCursor(0, 0)
	    lcd.print("T: %-3.1f /" % temperature)
	    lcd.print("H: %-3.1f " % humidity)

	    sleep(5)
	    
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

