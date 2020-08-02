import RPi.GPIO as GPIO
import dht11
import time
import datetime
import os

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
# read data using pin 4
instance = dht11.DHT11(pin=4)
'''
try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        cls()
	        print("Last valid input: " + str(datetime.datetime.now()))
	        print("Temperature: %-3.1f C" % result.temperature)
	        print("Humidity: %-3.1f %%" % result.humidity)
		
		
	    time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
'''
