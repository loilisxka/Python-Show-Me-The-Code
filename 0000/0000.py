from PIL import Image, ImageDraw, ImageFont


def image_add_num(pic_path, number=1):
    img = Image.open(pic_path)
    x_size, y_size = img.size
    font_size = x_size if x_size < y_size else y_size
    font_size /= 4
    my_font = ImageFont.truetype('Futura.ttf', size=int(font_size))
    number_txt = str(number) + ' ' if number < 100 else '99+'
    if my_font.getsize(number_txt)[0] > x_size or my_font.getsize(number_txt)[1] > y_size:
        return img
    position = x_size - my_font.getsize(number_txt)[0]
    ImageDraw.Draw(img).text((position, 0), number_txt, fill='red', font=my_font)
    return img

# test
image_add_num('ww.jpg').save('result.jpg', 'jpeg')
image_add_num('ww.jpg', 50).save('result50.jpg', 'jpeg')
image_add_num('ww.jpg', 100).save('result100.jpg', 'jpeg')
