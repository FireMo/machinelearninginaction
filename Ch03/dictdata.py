#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import random

# seze = ['青绿', '乌黑', '浅白']
# gendi = ['蜷缩', '稍蜷', '硬挺']
# qiaosheng = ['浊响', '沉闷', '清脆']
# wenli = ['清晰', '稍糊', '模糊']
# qibu = ['凹陷', '稍凹', '平坦']
# chugan = ['硬滑', '软粘']
# lab = ['yes', 'no']

seze = ['qinglv', 'wuhei', 'qianbai']
gendi = ['quansuo', 'shaoquan', 'yingting']
qiaosheng = ['zhuoxiang', 'chenmen', 'qingcui']
wenli = ['qingxi', 'shaohu', 'mohu']
qibu = ['aoxian', 'shaoao', 'pingtan']
chugan = ['yinghua', 'ruannian']
lab = ['yes', 'no']

listcan = []

y = open('listcan.txt', 'w')
y.truncate()
for a in seze:
    for b in gendi:
        for c in qiaosheng:
            for d in wenli:
                for e in qibu:
                    for f in chugan:
                        i = random.randint(0, 1)
                        listcan = '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (a, b, c, d, e, f, lab[i])
                        y.write(str(listcan))
y.close()


# for j in range(100):
#     i = random.randint(0, 1)
#     print i


