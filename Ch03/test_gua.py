# -*-coding:utf-8-*-
import trees
import treePlotter
from math import log
import operator
import urllib2
import chardet

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

# myDat, labels = trees.createDataSet()
# shannon = trees.calcShannonEnt(myDat)
# print shannon

# print trees.splitDataSet(myDat,0,1)
# print trees.chooseBestFeatureToSplit(myDat)


# def get_data():
#     fr = open('xiguadata2.txt')
#     lenses = [inst.strip().split('\t') for inst in fr.readlines()]
#     fp = open('xigualabel.txt')
#     # lensesLableses = [inst.strip().split('\t') for inst in fp.readlines()]
#     # lensesLables = lensesLableses[0]
#     lensesLables = ['seze', 'gendi', 'qiaosheng', 'wenli', 'qibu', 'chugan']
#     # lensesLables = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
#     # lensesLablestwo = lensesLables[:]
#     return lenses, lensesLables
lenses, lenses_lables = trees.get_data()
# print lenses
# print lenses_lables
lensesTree = trees.createTree(lenses, lenses_lables)
print lensesTree
print treePlotter.createPlot(lensesTree)


def data_deal():
    data_dict = {}
    lenses, lenses_labels = trees.get_data()
    for i in range(len(lenses_labels)):
        lc = [example[i] for example in lenses][0]
        # print lc[0].decode("ISO-8859-1")
        # print chardet.detect(lc[0])
        # print type(lc[0])
        lab_list = set([example[i] for example in lenses])
        data_dict[lenses_labels[i]] = lab_list
    return data_dict

# print data_deal()
# print chardet.detect(data_deal().keys()[0])


# def labels_value(ind):
#     lenses, lenses_labels = trees.get_data()
#     lab_list = set([example[ind] for example in lenses])
#     # for i in range(len(lenses_labels)):
#     #     labelsList = set([example[i] for example in lenses])
#     #     labList.append(labelsList)
#     return lab_list

# print labels_value(0)
# # for value in labelsValue(lenses)[0]:
# #     print type(value)
# print len(labels_value(0))


# def data_deal():
#     data_dict = {}
#     lenses, lenses_labels = trees.get_data()
#     for i in range(len(lenses_labels)):
#         lab_list = set([example[i] for example in lenses])
#         data_dict[lenses_labels[i]] = lab_list
#     return data_dict
#
# print data_deal()

# a = set("qinglv")
# a.add('qianbai')
# print a

