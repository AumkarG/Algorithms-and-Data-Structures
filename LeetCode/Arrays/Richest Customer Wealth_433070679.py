class Solution(object):
    def maximumWealth(self, accounts):
        s=0
        for i in accounts:
            s=max(s,sum(i))
        return s
        
