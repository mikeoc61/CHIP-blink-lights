#!/usr/bin/python

##########
# Michael O'Connor - 9/3/16
#
# 	Blinking LEDs program.
# 	Alternatively blinks 2 LEDs using GPIO logic on CHIP
# 	Watches for switch to pull input low and halts blinking until released
# 	CTRL-C to clean-up and exit
#
#	added extra comment line...
#
###########

#
import CHIP_IO.GPIO as GPIO
from time import sleep
#

# Define some stuff
Delay=0.2
LED1 = "XIO-P1"
LED2 = "XIO-P7"
Switch = "XIO-P0"

# Set up GPIO for desired use
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set initial state of LEDs to off
GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)

# Do something interesting
try:
   while True:
	while GPIO.input(Switch)==1:	# Loops while no switch
 	   sleep(Delay)
	   GPIO.output(LED1, GPIO.HIGH)	# Turn LED1 off
	   GPIO.output(LED2, GPIO.LOW)	# Turn LED2 on
	   sleep(Delay)
	   GPIO.output(LED1, GPIO.LOW)	# Turn LED1 on
	   GPIO.output(LED2, GPIO.HIGH)	# Turn LED2 off

	print("Thanks, I could use a break")	# Switch push detected

	while GPIO.input(Switch)==0:	# Loop while switch is pushed
           GPIO.output(LED1, GPIO.HIGH)	# LED1 off
           GPIO.output(LED1, GPIO.HIGH)	# LED2 off
	   sleep(Delay)
	print("Fine, Back to work!")	# Switch released

# Handler for CTRL-C
except KeyboardInterrupt:
	mystr = "\nLooks like it's time to bail. I'm outta here!"
	print(mystr)
	GPIO.output(LED1, GPIO.HIGH)
	GPIO.output(LED2, GPIO.HIGH)
	GPIO.cleanup()
