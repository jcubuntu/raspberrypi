import time
import Adafruit_SSD1306
from PIL import Image,ImageDraw,ImageFont

RST = 1
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
count = 0
while(1) :
	count = count+1
	width = disp.width
	height = disp.height
	image = Image.new('1', (width,height))	
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('VCR_OSD_MONO_1.001.ttf',14)
	draw.text((0,0), 'Hello World', font=font, fill=1)
	draw.text((0,30), str(count),font=font, fill=1)
	disp.image(image)
	disp.display()
