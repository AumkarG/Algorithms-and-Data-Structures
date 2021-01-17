class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=list(address)
        res=""
        for i in s:
            if i=='.':
                res+="[.]"
            else:
                res+=i
        return res
        
