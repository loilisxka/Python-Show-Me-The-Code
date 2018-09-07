# -*- coding: utf-8 -*-
import hmac

message = b'Hello,world'#先赋予一个根本的逻辑
with open('No.1_py.txt', 'w') as f:#打开文件
    for i in range(100, 300):
        i = str(i)#转换为字符串
        h = hmac.new(i.encode(encoding='utf-8'), message, digestmod = 'MD5')
        f.write('%s\n' % h.hexdigest())#将生成的激活码写入
