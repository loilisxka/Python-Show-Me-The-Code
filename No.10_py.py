# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndfont():
    return chr(random.randint(65, 90))

def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

wight = 60 * 4
high = 60
image = Image.new('RGB', (wight, high), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(wight):
    for y in range(high):
        draw.point((x,y), fill=rndcolor())
for i in range(4):
    draw.text((60*i+10, 10), rndfont(), font=font, fill=rndcolor2())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')