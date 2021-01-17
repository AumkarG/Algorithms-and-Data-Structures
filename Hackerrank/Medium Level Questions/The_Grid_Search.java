#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid, r,c):
    str=""
    for j in range(c):
        str+="O"
    grid1=[str]*r
    if(n%2==0):
        return grid1
    if(n==1):
        return grid
    i=2
    #pattern alternates after two explosions; ie the pattern after 3rd second and 5th second will keep repeating. If n= even ; grid is full.
    for i in range(r):
            for j in range(c):
                if(grid[i][j]=='O'):
                    grid1[i]=grid1[i][0:j]+'.'+grid1[i][j+1:]
                    if i!=r-1:
                         grid1[i+1]=grid1[i+1][0:j]+'.'+grid1[i+1][j+1:]
                    if i!=0:
                         grid1[i-1]=grid1[i-1][0:j]+'.'+grid1[i-1][j+1:]
                    if j!=c-1:
                         grid1[i]=grid1[i][0:j+1]+'.'+grid1[i][j+2:]
                    if j!=0:
                         grid1[i]=grid1[i][0:j-1]+'.'+grid1[i][j:]
    grid2=[str]*r
    for i in range(r):
            for j in range(c):
                if(grid1[i][j]=='O'):
                    grid2[i]=grid2[i][0:j]+'.'+grid2[i][j+1:]
                    if i!=r-1:
                         grid2[i+1]=grid2[i+1][0:j]+'.'+grid2[i+1][j+1:]
                    if i!=0:
                         grid2[i-1]=grid2[i-1][0:j]+'.'+grid2[i-1][j+1:]
                    if j!=c-1:
                         grid2[i]=grid2[i][0:j+1]+'.'+grid2[i][j+2:]
                    if j!=0:
                         grid2[i]=grid2[i][0:j-1]+'.'+grid2[i][j:]

    if(((n-1)/2)%2==1):
            return grid1
    else:
            return grid2
        
            
                
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid,r,c)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
