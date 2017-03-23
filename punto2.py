import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


pulsador = 4
segments =  (18,23,24,25,17,8,7)
# leds del display (a,b,c,d,e,f,g)
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)
    
#4 - 7pin fisico - pulsador
GPIO.setup(pulsador,GPIO.IN)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, 1)

valores = ('0','1','2','3','4','5','6','7','8','9')

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

def interrupcion(pulsador):
	global n
	n = n+1
	print ('interrupcion detectada')
	print (n)
    
try:
	GPIO.add_event_detect(pulsador, GPIO.RISING, callback=interrupcion, bouncetime=200)
	while True:
		for loop in range(0,7):
			GPIO.output(segments[loop],num[valores[n]][loop])
			    
		GPIO.output(22, 0)
		time.sleep(0.2)
		GPIO.output(22, 1)
		
finally:
    GPIO.cleanup()
