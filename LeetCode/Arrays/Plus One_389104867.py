class Solution(object):
    def plusOne(self, digits):
        x=int("".join([str(i) for i in digits]))
        x=x+1
        x=str(x)
        return([int(j) for j in x])
        
