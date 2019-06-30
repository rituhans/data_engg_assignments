# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:39:10 2019

@author: rhansraj
"""

myDict = { 'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango'}
inpStr = 'ilikesamsung'
#inpStr = 'likesam'
print("Input String :",inpStr)

mySmallDict = {x for x in myDict if x in inpStr}
#print(mySmallDict)

listOfDicWords = set()
isStringComplete=False
lastLen=-1
lastI=-1
i=0
l=1  

testStr = inpStr[i:i+l]

while len(testStr) > 0 and not isStringComplete:
    #print("Test String:", testStr, '\t i:',i,'\t l:',l)
    content = {x for x in mySmallDict if x.startswith(testStr)}
    #print('list:',content)
    if len(content) > 0:               
        for wrd in content:
            tempStr = inpStr[i:i+len(wrd)] 
            #print('tempStr:',tempStr)
            if tempStr == wrd:
                #print('word matched:',wrd)
                if wrd not in listOfDicWords:
                    listOfDicWords.add(wrd)
                if l==len(inpStr):
                    isStringComplete=True
                lastI=i
                lastLen=l
                l+=1
            else:
                #print('length of inp String', len(inpStr), ', length of test String:', len(testStr))
                if len(inpStr) > len(testStr):
                    l+=1
                elif len(inpStr) == len(testStr) and tempStr not in listOfDicWords:
                    #print('input string exhausted, no full match found')
                    isStringComplete=True
                    
    else:
        #print('in else',lastI,',',lastLen)
        if (i==lastI) and (lastI > -1) and (lastLen > -1) :
            #print('last word found was:', inpStr[lastI:lastLen])
            inpStr = inpStr[lastI+lastLen:len(inpStr)]
            i,l =0,1
            lastI, lastLen = -1, -1
            #print('New String :',inpStr)   
    testStr = inpStr[i:i+l]
            
     
print(listOfDicWords)
print('String Matched completely :',isStringComplete)
   