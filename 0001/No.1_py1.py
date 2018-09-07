# -*- coding: utf-8 -*-
import uuid#引入模块

def create_list(number = 200):
    list = []
    while True:#建立死循环
        jihuoma = str(uuid.uuid1()).replace('-', '')#生成激活码，且不带‘-’与‘’
        if jihuoma not in list:
            list.append(jihuoma)
        if len(list) == number:#打断循环
            break
    return list#返回列表
print(create_list())