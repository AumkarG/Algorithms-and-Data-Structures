import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        tot=0
        for i in nums:
            z=math.ceil(math.log(i,10))        
            if 10**z==i:
                z+=1
            if z%2==0:
                tot+=1
        return tot
