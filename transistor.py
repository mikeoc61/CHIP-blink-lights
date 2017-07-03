#!/usr/bin/python

##########
# Michael O'Connor - 9/3/16
#
# 	Transister switch prototype
#	User XIO to control BIAS to NPN transistor
# 	CTRL-C to clean-up and exit
#
###########

#
import CHIP_IO.GPIO as GPIO
from time import sleep
#

# Define some stuff
Delay=1.2
TRANS = "XIO-P4"
Switch = "XIO-P0"

# Set up GPIO for desired use
GPIO.setup(TRANS, GPIO.OUT)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set initial state of BIAS to off
GPIO.output(TRANS, GPIO.LOW)

# Do something interesting
try:
   while True:
	while GPIO.input(Switch)==1:	# Loops while no switch
 	   sleep(Delay)
	   print("Setting BIAS to HIGH")
	   GPIO.output(TRANS, GPIO.HIGH) # Raise to logic level 1
	   sleep(Delay)
	   print("Setting BIAS to LOW")
	   GPIO.output(TRANS, GPIO.LOW)	# Drop to logic level 0

	print("Thanks, I could use a break")	# Switch push detected

	while GPIO.input(Switch)==0:	# Loop while switch is pushed
           GPIO.output(TRANS, GPIO.LOW)	# LED1 off
	   sleep(Delay)

	print("Fine, Back to work!")	# Switch released

# Handler for CTRL-C
except KeyboardInterrupt:
	mystr = "\nLooks like it's time to bail. I'm outta here!"
	print(mystr)
	GPIO.output(TRANS, GPIO.LOW)
	GPIO.cleanup()
