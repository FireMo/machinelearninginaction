import regTrees
from numpy import *
from Tkinter import *

# testMat = mat(eye(4))
# print testMat[[0,2,3],:]
# print testMat.shape


# mat0,mat1 = regTrees.binSplitDataSet(testMat,1,0.5)
# print (testMat[:,1]>0.5)
# print (testMat[:,1]>0.5)[1][0]
# print nonzero(testMat[:,1] <= 0.5)[0]

# print mat0
# print '*****'
# print mat1

# myDat = regTrees.loadDataSet('ex00.txt')
# myMat = mat(myDat)
# print regTrees.createTree(myMat)

# myDat1 = regTrees.loadDataSet('ex0.txt')
# myMat1 = mat(myDat1)
# print regTrees.createTree(myMat1)

root = Tk()
myLabel = Label(root,text="Hello World")
myLabel.grid()
root.mainloop()
