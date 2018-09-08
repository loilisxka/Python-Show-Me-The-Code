# -*- coding: utf-8 -*-
import uuid
import mysql.connector
import pymysql#引入模块
#进行连接
conn = mysql.connector.connect(host='127.0.0.1',port=3306,user='root',password='password123',db='text',charset='utf8')
cursor = conn.cursor()#创建光标
cursor.execute('drop table if exists user')#删除表
cursor.execute('create table user(jhm char(35) not null,status char(1) not null)')#设置需要传入的数据大小
def create_number(number=200):#创建函数
    list = []
    while True:
        jhm = str(uuid.uuid1()).replace('-', '')
        if jhm not in list:
            list.append(jhm)#写入激活码
        if len(list) == number:
            break#打断循环
    return list
L = create_number()#得到列表
for i in L:#对列表进行循环
    try:
        cursor.execute("insert into user(jhm,status) values('%s','%s')" % (i, '0'))#对表进行插入
        conn.commit()#提交事务
        print('输入成功')
    except:
        print('输入失败')
cursor.close()#关闭光标
conn.close()#关闭连接