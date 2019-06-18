# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 00:18:30 2019

@author: rhansraj
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:19:10 2019

@author: rhansraj
"""
#noOfQrs = 0
#noOfComm = 0

lines = []

def readInput():
        
    N,Q = input().split()
    #print("No. of people :"+N)
    noOfQrs = int(Q)
    noOfComm = int(N)
    #print("No. of Queries :"+Q)
    
    for i in range(noOfQrs):
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    #text = '\n'.join(lines)
    #print(text)
    
    return noOfComm
    
def merge(people1,people2,nComm):
    #print("its Merge:", people1 , ", " , people2)
    for comm in nComm:
        if people1 in nComm[comm]:
            #print (people1, "in community ", comm)
            comm1 = comm
        elif people2 in nComm[comm]:
            #print (people2, "in community ", comm)
            comm2 = comm
    nComm[comm1] = nComm[comm1] | nComm[comm2]
    del nComm[comm2]
    #print("Comm combined :", nComm[comm1])
    #print("All Comm :", nComm)
    
def query(people, nComm):
    for comm in nComm:
        if people in nComm[comm]:
            #print(people, "in community", nComm[comm], "len : ", len(nComm[comm]))
            print(len(nComm[comm]))
        
def processMergeComm(noOfComms):
    
    nComm = {str(x): {str(x)} for x in range(1, noOfComms + 1)}
    #print("Initial Communities :", nComm)

    for line in lines:
    
        inpLine = line.split()
    
        if inpLine[0] == 'Q':
            query(inpLine[1], nComm)        
        elif inpLine[0] == 'M':
            merge(inpLine[1],inpLine[2], nComm)
    #print("Final Communities :", nComm)
    

noOfComms = readInput()
processMergeComm(noOfComms)


    