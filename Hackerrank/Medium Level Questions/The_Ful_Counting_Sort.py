#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    length=len(arr)
    count=0
    strings = [[] for _ in range(101)]
    for i in range(length//2):
        j=arr[i]
        l=int(j[0])
        s=j[1]
        strings[l].append('-')
    for k in range(length//2,length):
        m=arr[k]
        p=int(m[0])
        st=m[1]
        strings[p].append(st)
    for t in strings:
        for z in t:
          print(z,end="")
          print(" ",end="")
        
        



if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
