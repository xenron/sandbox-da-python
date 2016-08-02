import os
import numpy as np

#get data and augmented matrix
dataSet = []
file = open('data.txt')
for line in file.readlines():  
    lineArr = line.strip().split('\t')
    if int(lineArr[3]) == 1:  
        dataSet.append([float(lineArr[0]), float(lineArr[1]), float(lineArr[2]), float(1)])  
    if int(lineArr[3]) == -1:
        dataSet.append([(-1)*float(lineArr[0]), (-1)*float(lineArr[1]), (-1)*float(lineArr[2]), float(-1)])
##print dataSet

#initialize w[]
w = [0,0,0,0]

#begin the iteration
flag = False
count = 0
while(flag or count == 0):
    count += 1
    flag = False
    for i in xrange(len(dataSet)):
        label = 0
        temp = dataSet[i]
        for j in xrange(len(w)):
            label += w[j]*temp[j]
        if(label > 0):
            print(w)
        else:
            print("w is changed:")
            for k in xrange(len(w)):
                w[k] += temp[k]
            print(w)
            flag = True
print("the count of iteration is " + repr(count))
print("the final w is:")
print(w)

