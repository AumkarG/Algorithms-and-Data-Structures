class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow=[0]*26
        for i in allowed:
            allow[ord(i)-97]=1
        tot=0
        for i in words:
            flag=0
            for j in i:
                if allow[ord(j)-97]!=1:
                    flag=1
                    break
            if flag==0:
                tot+=1
        return tot
            
        
