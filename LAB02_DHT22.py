import Adafruit_DHT
import time

dhtType = Adafruit_DHT.DHT22
dhtPin = 10

while True:
	humid, temp = Adafruit_DHT.read_retry(dhtType, dhtPin)
	print('Temp : %0.1f'% temp)
	print('Humid : %0.1f'% humid)
	time.sleep(2)
