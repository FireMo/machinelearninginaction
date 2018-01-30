# encoding=utf-8
import trees
import treePlotter
from math import log
import operator
import urllib2

# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

# myDat, labels = trees.createDataSet()
# shannon = trees.calcShannonEnt(myDat)
# print shannon

# print trees.splitDataSet(myDat,0,1)
# print trees.chooseBestFeatureToSplit(myDat)

fr = open('xiguadata2.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
fp = open('xigualabel.txt')
# lensesLableses = [inst.strip().split('\t') for inst in fp.readlines()]
# lensesLables = lensesLableses[0]
lensesLables = ['seze', 'gendi', 'qiaosheng', 'wenli', 'qibu', 'chugan']
# lensesLables = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
lensesLablestwo = lensesLables[:]
lensesTree = trees.createTree(lenses, lensesLables)
print lensesTree
print treePlotter.createPlot(lensesTree)

# print trees.classify(lensesTree, lensesLablestwo, ['qinglv', 'quansuo', 'zhuoxiang', 'mohu', 'aoxian', 'yinghua'])






# request = urllib2.Request("http://www.baidu.com")
# response = urllib2.urlopen(request)
# print response.read()


