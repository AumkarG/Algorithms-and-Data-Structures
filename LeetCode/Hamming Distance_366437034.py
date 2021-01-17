class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s="{0:b}".format(x^y)
        sm=0
        for i in s:
            sm+=int(i)
        return sm
