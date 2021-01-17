class Solution(object):
    def shuffle(self, nums, n):
        res=[-1]*n*2
        l=len(nums)
        for i in range(l/2):
            res[2*i]=nums[i]
        for i in range(l/2,l):
            res[2*(i-l/2)+1]=nums[i]
        return res
            
