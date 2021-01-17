class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res=""
        res1=""
        for i in word1:
            res+=i
        for i in word2:
            res1+=i
        return res==res1
