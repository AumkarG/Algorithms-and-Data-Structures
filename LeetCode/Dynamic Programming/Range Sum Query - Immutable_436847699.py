class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=nums
        self.sm=[0]*len(nums)
        if len(nums)>0:
            self.sm[0]=nums[0]
            for i in range(1,len(nums)):
                self.sm[i]=self.sm[i-1]+self.arr[i]


    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.sm[j]
        else:
            return self.sm[j]-self.sm[i-1]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
