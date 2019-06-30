# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 00:20:15 2019

@author: rhansraj
"""

#inpList = [7,2,-1,2]
#inpList = [-3,7,-2,3,5,-2]
inpList = [5,7,-5,6,3,9,-8,2,-1,10]
listOfSubArr = []

def calcPairSum(tempList):
    a=0
    b=len(tempList)
    sum=0
    #print(tempList)
    while a < len(tempList):
        b=len(tempList)
        c=a+1
        while c < b :
            #print('a:',a,', c:',c, ':', tempList[a], ',', tempList[c], ', Sum:',int(tempList[a]) * int(tempList[c]))
            sum = sum + int(tempList[a]) * int(tempList[c])
            c+=1
        a+=1       
    #print('Sum : ', sum)    
    return sum        

def createSubArrays(tempList):
    a=0
    b=len(tempList)
    print(tempList)
    while a < len(tempList):
        #b=len(tempList)
        c=a+1
        while c <= b :
            if a+1 != c:
                print('a:',a,', c:',c, ':', tempList[a:c])
                listOfSubArr.append(tempList[a:c])
            c+=1
        a+=1  
        
     
def calLargestPair():
    lstSum = 0
    maxI = 0
    for i in range(len(listOfSubArr)):
        if i==0 :
            lstSum = calcPairSum(listOfSubArr[i])
        else:
            tmpSum = calcPairSum(listOfSubArr[i])
            if tmpSum > lstSum:
                lstSum = tmpSum
                maxI = i
    
    print('final largest sum:', lstSum)
    print('List : ',listOfSubArr[maxI])
    
    
createSubArrays(inpList)
#print(*listOfSubArr, sep = "\n") 
calcPairSum(listOfSubArr[0])
calLargestPair()
    
    




    
    
    