import random
import re
import os

WORDS = ["SWITCH","LIGHT", "ON","OFF","BLINKING"]
PRIORITY = 20

def handle(text, mic, profile):
   try:
			        

	cmd = 'sudo python /home/pi/OZ_pi/Lamp.py -i '
  	if bool(re.search(r'\b(light on|\son\s.*light)\b', text, re.IGNORECASE)):
		mic.say('light now is on')
		os.system(cmd+"switch on")
    	elif bool(re.search(r'\b(light off?|\soff?\s.*light)\b', text, re.IGNORECASE)):
    	 	mic.say('light now is off')
       		os.system(cmd+"switch off")
    	else:
		mic.say('light now is blinking 5 times')
		os.system(cmd+"blink 5 1")

    	mic.say('DONE... ')
   
   except:
	print "Lighting Error"
   	mic.say('Sorry... something wrong on lighting configuration')
  

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """

    if bool(re.search(r'\b(light on|light off?|\soff?\s.*light|\son\s.*light|blinking|light blinking|blinking\s.*light)\b', text, re.IGNORECASE)):
    	return True
    
    return False
