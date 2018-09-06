# -*- coding: utf-8 -*-
from PIL import ImageFont, ImageDraw, Image

def create_img(pic_path, number=1):
    img = Image.open(pic_path)
    x_size, y_size = img.size
    if x_size > y_size:
        font_size = x_size
    else:
        font_size = y_size
    font_size /= 4
    number_size = ImageFont.truetype('/Users/yyy/Documents/GitHub/Python-Show-Me-The-Code/0000/Futura.ttf', size=int(font_size))
    if number < 100:
        number_txt = str(number)
    elif number >= 100:
        number_txt = str('99+')
    if number_size.getsize(number_txt)[0] > x_size or number_size.getsize(number_txt)[1] > y_size:
        return img
    pos = x_size - number_size.getsize(number_txt)[0]
    ImageDraw.Draw(img).text((pos, 0), number_txt, fill='red', font=number_size)
    return img
create_img('ww.jpg').save('1.jpg')
create_img('ww.jpg', 50).save('50.jpg')
create_img('ww.jpg', 100).save('100.jpg')