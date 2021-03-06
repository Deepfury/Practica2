import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

segments =  (18,23,24,25,17,8,7)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

digits = (22,10,9,11) 

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
    

num = {'0':(0,0,0,0,0,0,1),
    '1':(1,0,0,1,1,1,1),
    '2':(0,0,1,0,0,1,0),
    '3':(0,0,0,0,1,1,0),
    '4':(1,0,0,1,1,0,0),
    '5':(0,1,0,0,1,0,0),
    '6':(1,1,0,0,0,0,0),
    '7':(0,0,0,1,1,1,1),
    '8':(0,0,0,0,0,0,0),
    '9':(0,0,0,1,1,0,0)}

try:
	while True:
		n = time.ctime()[11:13]+time.ctime()[14:16]
		s = str(n).rjust(4)
		for digit in range(4):
			for loop in range(0,7):
				GPIO.output(segments[loop], num[s[digit]][loop])
			GPIO.output(digits[digit], 0)
			time.sleep(0.002)
			GPIO.output(digits[digit], 1)
finally:
    GPIO.cleanup()
