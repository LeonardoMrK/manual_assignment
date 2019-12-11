#!/usr/bin/env python
# coding: utf-8
# @Author  : Mr.K
# @Software: PyCharm Community Edition
# @Time    : 2019/12/4 16:24
# @Description: 读取"标注文件.txt"文件，逐行对比，根据正则表达式匹配标签，把数据分开存放
#0标签是食物，1标签是添加物，2是其他

import re
output_path='D:\project\pycharmworkspace\\tag_assignment\output\\'

with open("tag_data_V1.0/0.txt",'r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        # print(line)
        if not line:
            break
        elif re.match(r'0.*',line):#正则匹配0标签的内容（食品）
            f1 = open(output_path+'0.txt', 'a')#新建文本文件
            f1.write(line)#写入
            f1.close()#一定要关闭，不然写不进去
        elif re.match(r'1.*',line):#正则匹配1标签的内容（添加剂）
            f2 = open(output_path+'1.txt', 'a')
            f2.write(line)
            f2.close()
        elif re.match(r'2.*',line):#正则匹配2标签的内容（其他）
            f3=open(output_path+'2.txt','a')
            f3.write(line)
            f3.close()
        else:  #无标签句子
            f4 = open(output_path + '3.txt', 'a')
            f4.write(line)
            f4.close()