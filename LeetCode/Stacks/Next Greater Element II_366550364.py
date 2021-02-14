class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        great=[-1]*n
        stack.append(0)
        i=1
        while(len(stack)!=0 and i<n):
            while(len(stack)!=0):
                if(nums[i]>nums[stack[len(stack)-1]]):
                    great[stack.pop()]=nums[i]
                else:
                    break
            stack.append(i)
            i+=1
        for i in range(n):
                while(len(stack)!=0):
                    if(nums[i]>nums[stack[len(stack)-1]]):
                        great[stack.pop()]=nums[i]
                    else:
                        break
        return great
