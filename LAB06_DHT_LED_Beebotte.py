import Adafruit_DHT
from beebotte import *
import RPi.GPIO as GPIO

# Replace with your API, SECRET_KEY, CHANNEL, RESOURCE
API_KEY = '7ffbd7b021342ea34c2c88b152b150e8'
SECRET_KEY = '943b8f00ba4ae1dc293be1e26f5599bd485d06d595bcb1a3a655d6f0eeb8638e'

CHANNEL = 'dhtChanel'
HUMI_RESOURCE_NAME = 'humid'
TEMP_RESOURCE_NAME = 'temp'
LED_RESOURCE_NAME = 'led_state'

bbt = BBT(API_KEY,SECRET_KEY)
period = 5 ## Sensor data reporting period (5 second)

# Init DHT Type, DHT Pin
DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN = 10

# LED Setting
LED_PIN = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
    if humidity is not None and temperature is not None:
		print('Temp : %0.1f'% temperature)
		print('Humid : %0.1f'% humidity)
		try:
			bbt.write(CHANNEL, TEMP_RESOURCE_NAME, temperature)
			bbt.write(CHANNEL, HUMI_RESOURCE_NAME, humidity)
		except Exception:
			print("Error while writing to Beebotte")
    else:
        print("Failed to get reading. Try again!")

    ledState = bbt.read(CHANNEL, LED_RESOURCE_NAME, 1)[0]['data']
    GPIO.output(LED_PIN, ledState)
    time.sleep(period)
