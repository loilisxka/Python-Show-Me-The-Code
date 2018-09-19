# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup                   #引入模块

def search(path):
    with open(path, encoding='utf-8') as f:     #以utf-8编码打开文件
        text = BeautifulSoup(f, 'html.parser')  #使用python默认的html.parser编译器
        urls = text.find_all('script')          #找出所有script标签
        for u in urls:
            print(u['src'])                     #打印连接
        content = text.get_text().strip('\n')
    return content