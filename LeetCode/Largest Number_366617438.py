
def custom_compare(x, y):
    return int(x+y)-int(y+x)

class Solution(object):
    def largestNumber(self, nums):
        nums=[str(i) for i in nums]
        nums=sorted(nums, cmp=custom_compare,reverse=True)
        if(nums[0]=='0'):
            return '0'
        s=""
        for i in nums:
            s+=i
        return s
