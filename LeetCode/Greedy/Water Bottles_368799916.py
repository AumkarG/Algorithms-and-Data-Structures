class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        e=numBottles
        d=numBottles
        while(e>=numExchange):
            x=e//numExchange
            e-=x*numExchange
            d+=x
            e+=x
        return d
