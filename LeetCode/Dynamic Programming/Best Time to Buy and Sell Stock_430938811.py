class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mnm=10001
        prof=0
        for i in prices:
            if i-mnm>prof:
                prof=i-mnm
            elif i<mnm:
                mnm=i
        return prof
            
