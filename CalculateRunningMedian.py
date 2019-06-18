# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 01:22:50 2019

@author: rhansraj
"""

lines = []

def readInput():
        
    N = input()
    #print("No. of people :"+N)
    listCount = int(N)
    #print("No. of Queries :"+Q)
                   
    for i in range(listCount):
        line = input()
        if line:
            lines.append(line)
        else:
            break
        
def calcRunningMedian():
    runnNoList = []
    sortedNoList = []
    runnMedList = []
    
    for line in lines:
        runnNoList.append(int(line))
        sortedNoList = sorted(runnNoList)
        listCount = len(sortedNoList)
        if  listCount % 2 == 0:
            L1 = (listCount/2) -1
            L2 = (listCount/2)
            RM = (sortedNoList[int(L1)] + sortedNoList[int(L2)])/2
            #print("Running Med Even: {0.1f}" % RM)
            #print("{0:.1f}".format(RM))
            #print(format(RM, '.1f'))
            runnMedList.append(format(RM, '.1f'))
            #runnMedList.append(RM)
        else:
            L = (listCount/2)
            RM = sortedNoList[int(L)]
            #print("Running Med Odd:", RM)
            #print("{0:.1f}".format(RM))
            #print(round(RM,2))
            #print(format(RM, '.1f'))
            runnMedList.append(format(RM, '.1f'))
    
    print('\n'.join(map(str, runnMedList)))
        
readInput()
calcRunningMedian()        
