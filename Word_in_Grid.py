# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:24:52 2019

@author: rhansraj
"""

grid = ["axmy", "bgdf", "xeet", "raks"]
#grid = ["axmy", "brdf", "xeet", "rass"]
word = "geeks"
print('Search Word :',word)

def checkFullString(row,col,char):
    #print('Current Char of word:', word[char])
                    
    #left value
    if col-1 > -1 and char+1 < len(word) and grid[row][col-1] == word[char+1]:
        checkFullString(row,col-1,char+1)
    #right value
    elif col+1 <= colLength and char+1 < len(word) and grid[row][col+1] == word[char+1]:
        checkFullString(row,col+1,char+1)
    #up value
    elif row-1 > -1 and char+1 < len(word) and grid[row-1][col] == word[char+1]:
        checkFullString(row-1,col,char+1)
    #down value
    elif row+1 <= rowLength and char+1 < len(word) and grid[row+1][col] == word[char+1]:
        checkFullString(row+1,col,char+1)
    else:
        if char+1 == len(word):
            print('Word Found')
        else:
            print('Word not Found')

isFirstCharFound = False
rowLength = len(grid)
colLength = 0
if len(grid[0]) > 0:
    colLength = len(grid[0])

for i in range(len(grid)):
    #print(grid[i])    
    for j in range(len(grid[i])):
        #print(grid[i][j])
        if word.startswith(grid[i][j]):
            #print('Start Char Found')
            checkFullString(i,j,0)
            isFirstCharFound = True
            break
    if isFirstCharFound:
        break
                    
if not isFirstCharFound:
    print('Word not Found')
    

