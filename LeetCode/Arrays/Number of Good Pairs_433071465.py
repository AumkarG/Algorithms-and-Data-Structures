from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        c=Counter(nums)
        tot=0
        for i in c:
            if c[i]>=2:
                tot+=(c[i]*(c[i]-1))/2
        return tot
        
