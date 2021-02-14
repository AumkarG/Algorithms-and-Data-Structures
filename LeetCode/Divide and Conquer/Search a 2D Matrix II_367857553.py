class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        if(m==0):
            return False
        n=len(matrix[0])
        if(n==0):
            return False
        col=n-1
        row=0
        while(col>=0 and row<m):
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                col-=1
            else:
                row+=1
        return False
