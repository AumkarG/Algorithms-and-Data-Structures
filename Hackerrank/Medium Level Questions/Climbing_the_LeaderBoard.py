#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    m=len(alice)
    n=len(scores)
    pos=1
    k=0
    res=[]
    count=0
    x=0
    for x in range(n):
        if(alice[0]>=scores[x]):
            res.append(pos)
            count+=1
            break
        elif(x==n-1 or scores[x]>scores[x+1]):
            pos+=1
    if(count==0):
        res.append(pos)
    if(x==n-1 and count==0):
      n=x+1;
    else:
      n=x;
    i=1
    while(i<m):
        k=n
        while(n>0 and scores[n-1]<=alice[i]):
            n-=1
            if(n+1==k or scores[n]>scores[n+1]):
                 pos-=1
        res.append(pos)
        i+=1
    return res


    

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))

