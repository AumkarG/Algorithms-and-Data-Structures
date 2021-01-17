class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        c=[0]*l
        c[0]=cost[0]
        c[1]=cost[1]
        for i in range(2,l):
            c[i]=min(c[i-1],c[i-2])+cost[i]
        
        return min(c[l-1],c[l-2])
            
