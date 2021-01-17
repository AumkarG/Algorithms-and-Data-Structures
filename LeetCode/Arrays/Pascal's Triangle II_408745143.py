class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return[1]
        elif rowIndex==1:
            return [1,1]
        else:
            start=[1,1]
            for i in range(2,rowIndex+1):
                x=[0]*(i+1)
                x[0]=1
                x[i]=1
                for j in range(len(start)-1):
                    x[j+1]=start[j]+start[j+1]
                start=x
            return start
