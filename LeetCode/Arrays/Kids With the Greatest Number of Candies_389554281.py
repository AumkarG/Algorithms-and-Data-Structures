class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest=max(candies)
        res=[]
        for i in candies:
            if(i+extraCandies)>=highest:
                res.append(True)
            else:
                res.append(False)
        return res
