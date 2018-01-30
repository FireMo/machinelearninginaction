import kNN
import operator

group,labels = kNN.createDataSet()
# print group
# print labels

# Test the hypothetical data
# print kNN.classify0([0.5,0.5],group,labels,3)

# Converts text records to NumPy
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
# datingDataMat = [[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]]



# print datingDataMat[:,0]
# print datingLabels[0:20]

# normMat,ranges,minVals = kNN.autoNorm(datingDataMat)
# print normMat
# print ranges
# print minVals

kNN.creatPlot(datingDataMat,datingLabels)

# kNN.datingClassTest('datingTestSet2.txt')

# testVector = kNN.img2vector('testDigits/0_13.txt')
# print testVector[0,0:32]

# kNN.handwritingClassTest()