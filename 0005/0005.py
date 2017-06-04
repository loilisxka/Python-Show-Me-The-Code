from PIL import Image
from os import listdir

def change_image_size(path, size=(1136, 640)):
    image_files = [image_file for image_file in listdir(path)]
    for image_file in image_files:
        image_abs_file = path + '/' + image_file
        image = Image.open(image_abs_file)
        size = (size[1], size[0]) if size[1] > size[0] else size
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(path + '/result_' + image_file)

change_image_size('./images')