# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 22:30:22 2019

@author: rhansraj
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:20:32 2019

@author: rhansraj
"""

listOfNo = [100,80,60,70,60,75,85]
spanList = []

print(listOfNo)

for i in range(0,len(listOfNo)):
    currNo = listOfNo[i]
    span = 1
    for j in range(i,0,-1):
        if currNo > listOfNo[j-1]:
            span+=1
        else:
            break
    spanList.append(span)
    
print(spanList)
        