import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
while True:
	GPIO.output(24, 0)
	print('GPIO24=OFF')
	time.sleep(1)
	GPIO.output(24, 1)
	print('GPIO24=ON')
	time.sleep(1)
