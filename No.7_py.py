# -*- coding: utf-8 -*-
import os

dit = {'hangshu': 0, 'zhushi': 0, 'konghang': 0}
for f in os.listdir('.\python'):
    i = open('python/%s' % f, encoding='utf-8', errors='ignore')
    for x in i.readline():
        if x is None:
            dit['konghang'] += 1
        if '#' in x:
            dit['zhushi'] += 1
        else:
            dit['hangshu'] += 1
    i.close()
print(dit)