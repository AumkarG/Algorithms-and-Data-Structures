class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        swap=False
        l=len(nums)
        for i in range(1,l):
            if(nums[l-1-i]<nums[l-i]):
                swap=True
                idx=l-1-i
                break       
        if(swap==False):
            return nums.reverse()        
        for j in range(idx+1,l):
            if(nums[j]>nums[idx]):
                ix=j
        temp=nums[ix]
        nums[ix]=nums[idx]
        nums[idx]=temp
        t=nums[idx+1:]
        t.reverse()
        nums[idx+1:] = t

