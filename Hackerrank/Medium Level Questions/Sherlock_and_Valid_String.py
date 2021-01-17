
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    freq=[0]*26
    for i in s:
        freq[ord(i)-97]+=1
    distinct=[]
    count=[]
    for j in freq:                                  #calculate frequency of each alphabet
        if(j!=0):
            if(j not in distinct):                  
                distinct.append(j)
                count.append(1)
            else:
                count[distinct.index(j)]+=1
    if(len(count)>2):
        return "NO"
    if(len(count)==1):
        return "YES"
    else:
        if(count[0]<count[1]):
            low=0
            high=1
        else:
            low=1
            high=0
        if(count[low]>1):
            return "NO"
        if(distinct[low]>distinct[high] and distinct[low]-distinct[high]==1):
            return "YES"
        elif(distinct[low]==1):
            return "YES"
        else:
            return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
