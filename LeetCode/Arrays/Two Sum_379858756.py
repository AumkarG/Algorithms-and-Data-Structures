class Solution(object):
    def twoSum(self, nums, target):
        A=dict()
        for i in range(len(nums)):
            if (target-nums[i]) in A:
                return [A[target-nums[i]],i]
            else:
                A[nums[i]]=i
                
