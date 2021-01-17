class Solution(object):
    def countVowelStrings(self, n):
        ls=[1]*5
        for k in range(2,n+1):
            for i in range(5):
                tot=0
                for j in range(i,5):
                    tot+=ls[j]
                ls[i]=tot
        return sum(ls)
