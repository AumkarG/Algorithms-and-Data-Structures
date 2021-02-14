class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sm=0
        for i in range(k):
            sm+=cardPoints[i]
        s=sm
        for j in range(1,k+1):
            s+=cardPoints[-j]-cardPoints[k-j]
            if(s>sm):
                sm=s
        return sm
        
