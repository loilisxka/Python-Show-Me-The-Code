# -*- coding: utf-8 -*-
import redis
import uuid

conn = redis.Redis(host='127.0.0.1',
                   port=6379,
                   db=0)

def create_number(number=200):
    list = []
    while True:
        jihuoma = str(uuid.uuid1()).replace('-', '')
        if jihuoma not in list:
            list.append(jihuoma)
        if len(list) == number:
            break
    return list

L = create_number()

for i, e in enumerate(L):
    try:
        conn.set(i, e)
        print('输入成功')
    except:
        print('输入失败')