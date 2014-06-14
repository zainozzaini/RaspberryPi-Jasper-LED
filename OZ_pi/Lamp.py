#! /usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'
import sys, getopt

#GPIO.cleanup()
GPIO.setwarnings(False)


## Define function named Blink()
def Blink(numTimes, speed):
    for i in range(0,numTimes): ## Run loop numTimes
        print "Iteration " + str(i+1) ##Print current loop
        GPIO.output(7, True) ## Turn on GPIO pin 7
        time.sleep(speed) ## Wait
        GPIO.output(7, False) ## Switch off GPIO pin 7
        time.sleep(speed) ## Wait
    print "Done" ## When loop is complete, print "Done"
    GPIO.cleanup()


## ON OFF Function
def Switch(power):
   if power:
	GPIO.output(7, True)
	print 'lamp on'

   else:
	GPIO.output(7, False)
	GPIO.cleanup()
	print 'lamp off'

def main(argv):
   GPIO.cleanup()
   GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
   GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT
   type = ''
   try:
      opts, args = getopt.getopt(argv,"i:p:h",['input=', 'params=', 'help'])
   except getopt.GetoptError:
      print 'Wrong command'
      sys.exit(2)
   print opts,args

   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         input = arg

         if input == 'switch' :
		#print opts,args[0]
		if args[0] == 'on':
			Switch(True)
		elif args[0] == 'off':
			Switch(False)
		else:
			print 'Please choose on or off'
	 elif input == 'blink':
		## Prompt user for input
		if len(args)==2 :
			iterations = args[0]
			speed = args[1]
		else:
			iterations = raw_input("Enter the total number of times to blink: ")
			speed = raw_input("Enter the length of each blink in seconds: ")
		## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
		Blink(int(iterations),float(speed))
		## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters

      

#if __name__ == "__main__":
try:
	main(sys.argv[1:])
except:
	GPIO.cleanup()
	print 'error in main block'
