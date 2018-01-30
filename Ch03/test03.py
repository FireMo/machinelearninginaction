# encoding=utf-8
import trees
import treePlotter
from math import log
import operator
import urllib2
import numpy as np
import matplotlib.pyplot as pl

# import matplotlib
# matplotlib.use('qt4agg')
# # 指定默认字体
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['font.family'] = 'sans-serif'
# # 解决负号'-'显示为方块的问题
# matplotlib.rcParams['axes.unicode_minus'] = False
# pl.plot([-1, 2, -5, 3])
# pl.title(u'中文')
# pl.show()



# from matplotlib.font_manager import FontProperties
# import matplotlib.pyplot as plt
#
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
#
# plt.xlabel(u"电压差(V)", fontproperties=font)
# plt.ylabel(u"介质损耗角差(度)", fontproperties=font)
# plt.title(u"介质损耗角和荷电状态SOC关系图", fontproperties=font)
# plt.show()


# import matplotlib.pyplot as plt
#
# plt.xlabel(u'x轴')
#
# plt.ylabel(u'y轴')
#
# plt.bar(left = (0,1),height =(1,0.5),width = 0.35)
#
# plt.show()

myDat, labels = trees.createDataSet()
# print trees.createTree(myDat, labels)

# print labels
# myTree = treePlotter.retrieveTree(0)
# print myTree
# print trees.classify(myTree, labels, [1, 0])
# print trees.classify(myTree, labels, [1, 1])

# shannon = trees.calcShannonEnt(myDat)
# print shannon

# print trees.splitDataSet(myDat,0,1)
# print trees.chooseBestFeatureToSplit(myDat)

# fr=open('lenses.txt')
# lenses=[inst.strip().split('\t') for inst in fr.readlines()]
# lensesLables=['age', 'prescript', 'astigmatic', 'tearRate']
# lensesTree = trees.createTree(lenses, lensesLables)
# # print lensesTree
# # print treePlotter.createPlot(lensesTree)
# fig = treePlotter.createPlot(lensesTree)








