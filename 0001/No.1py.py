# -*- coding: utf-8 -*-
import hmac

message = b'Hello,world'
with open('No.1_py.txt', 'w') as f:
    for i in range(100, 300):
        i = str(i)
        h = hmac.new(i.encode(encoding='utf-8'), message, digestmod = 'MD5')
        f.write('%s\n' % h.hexdigest())
