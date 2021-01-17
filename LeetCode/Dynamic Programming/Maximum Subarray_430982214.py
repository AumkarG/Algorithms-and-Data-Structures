class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[0]
        ans=prev
        for i in range(1,n):
            prev=max(nums[i],nums[i]+prev)
            ans=max(ans,prev)
        return ans
