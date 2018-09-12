# -*- ;coding utf-8 -*-
from PIL import Image                       #引入模块
import os

n = 0
for each in os.listdir('./images'):         #循环文档中的每个文件
    pic = Image.open('images/%s' % each)    #打开图片文件
    w, h = pic.size                         #获得尺寸数据
    if w == 640 and h == 1136:
        print("无需操作")
        break
    else:
        pic.thumbnail((640, 1136))          #改变尺寸大小
        n += 1
        pic.save('%s.png' % n)              #进行保存
