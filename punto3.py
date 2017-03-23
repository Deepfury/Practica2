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
    
#configuracion de entrada del pulsador   
pulsador = 4
GPIO.setup(pulsador,GPIO.IN)

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
    
n=0
contador=0

def interrupcion(pulsador): #funcion que llama el evento de interrupcion
	global n
	global contador
	contador = 0
	n = 0
	print ('interrupcion detectada')
	print (n)


try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	while True:
		s = str(n).rjust(4,'0')
		for digit in range(4):
			for loop in range(0,7):
				GPIO.output(segments[loop], num[s[digit]][loop])
				
			GPIO.output(digits[digit], 0)
			time.sleep(0.001)
			contador=contador+1
			GPIO.output(digits[digit], 1)
			
		if (contador == 60000):	
			n=n+1
			contador=0
		
finally:
    GPIO.cleanup()
