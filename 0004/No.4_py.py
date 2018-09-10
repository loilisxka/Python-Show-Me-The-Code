# -*- coding: utf-8 -*-

dit = {}                                                        #创建空字典
ignore = [',', '.', '\n', '\'', '\"', '!', '?', '1',            #确定需要忽略的字符
          '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
text = open('input.txt').read()                                 #打开文本

for i in ignore:
    text = text.replace(i, '')                                  #将需要忽略的字符替换为空
text = text.lower()                                             #全改为小写，方便计数

for word in text:                                               #开始计数
    if word not in dit:
        dit[word] = 1
    else:
        dit[word] += 1

print(dit)                                                      #输出结果