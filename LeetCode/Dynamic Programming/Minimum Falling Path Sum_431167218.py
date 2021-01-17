class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        curr=A[0]
        n=len(A[0])
        for i in range(1,len(A)):
            nw=A[i]
            for j in range(n):
                nw[j]=nw[j]+min(curr[max(0,j-1):min(j+2,n)])
            curr=nw
        return min(curr)
                    
        
        
