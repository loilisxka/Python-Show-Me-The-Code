# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def get_body(path):
    with open(path, encoding='utf-8') as f:
        text = BeautifulSoup(f, 'html.parser')
        urls = text.find_all('body')
        for u in urls:
            print(u)
        content = text.get_text().strip('\n')
    return content

get_body('py.html')