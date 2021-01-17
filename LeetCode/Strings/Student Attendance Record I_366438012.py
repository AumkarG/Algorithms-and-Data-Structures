class Solution:
    def checkRecord(self, s: str) -> bool:
        A=0
        n=len(s)
        for i in range(n):
            if(s[i]=='A'):
                A+=1
            else:
                if(i>1 and s[i]==s[i-1]==s[i-2]=='L'):
                    return False
            if(A>1):
                return False
        return True
        
