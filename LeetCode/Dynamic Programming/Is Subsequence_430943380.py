class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        n=len(s)
        if n==0:
            return True
        for i in t:
            if(s[j]==i):
                j+=1
                if(j==n):
                    break
        return j==n
                    
        
