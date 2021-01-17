class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tot=0
        l=0
        r=0
        for i in s:
            if i=='L':
                l+=1
            else:
                r+=1
            if(l==r):
                l=0
                r=0
                tot+=1
        return tot
        
