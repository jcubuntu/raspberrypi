import Adafruit_DHT
from beebotte import *

# Replace with your API, SECRET_KEY, CHANNEL, RESOURCE
API_KEY = '7ffbd7b021342ea34c2c88b152b150e8'
SECRET_KEY = '943b8f00ba4ae1dc293be1e26f5599bd485d06d595bcb1a3a655d6f0eeb8638e'

CHANNEL = 'dhtChanel'
HUMI_RESOURCE_NAME = 'humid'
TEMP_RESOURCE_NAME = 'temp'

bbt = BBT(API_KEY,SECRET_KEY)
period = 5 ## Sensor data reporting period (5 second)

# Init DHT Type, DHT Pin

dhtType = Adafruit_DHT.DHT22
dhtPin = 10

while True:                                                          
	humidity, temperature = Adafruit_DHT.read_retry(dhtType, dhtPin)
	if humidity is not None and temperature is not None:
		
		print('Temp : %0.1f'% temperature)
		print('Humid : %0.1f'% humidity)
		try:
			#Send temperature to Beebotte
			bbt.write(CHANNEL, TEMP_RESOURCE_NAME, temperature)
			#Send hu000midity to Beebotte
			bbt.write(CHANNEL, HUMI_RESOURCE_NAME, humidity)
		except Exception:
			##Process exception here
			print("Error while writing to Beebotte")
	else:
		print("Failed to get reading. Try again!")
	#Sleep some time
	time.sleep(period)
