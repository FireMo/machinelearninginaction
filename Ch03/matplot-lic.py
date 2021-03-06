# encoding=utf-8

import matplotlib.pyplot as plt

# from pylab import *
# mpl.rcParams['font.sans-serif'] = ['SimHei']

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def createPlot():
   fig = plt.figure(1, facecolor='white')
   fig.clf()
   createPlot.ax1 = plt.subplot(111, frameon=False)  # ticks for demo puropses
   plotNode(u'决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
   plotNode(u'叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
   plt.show()

# print createPlot()

d = {u'\u5e7f\u4e1c': 2, '\xe5\x8c\x97\xe4\xba\xac': 55, u'\u5317\u4eac': 8, u'\u53f0\u6e7e': 1, u'\u798f\u5efa': 2, u'\u6d59\u6c5f': 2}
# for k,v in d.items():
#     print k,v

import json
result = json.dumps(d, encoding='UTF-8', ensure_ascii=False)
# print d
for k,v in d.items():
    print k,v