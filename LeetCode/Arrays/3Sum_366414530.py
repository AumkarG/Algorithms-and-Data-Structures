class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        res=[]
        lg=len(nums)
        while(i<lg-2 and nums[i]<=0):
            if(i>0 and nums[i]==nums[i-1]):
                i+=1
                continue
            
            l=i+1
            r=lg-1
            while(l<r):
                s=nums[i]+nums[l]+nums[r]
                if(s<0):
                    l+=1
                elif(s>0):
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l+1]==nums[l]):
                        l+=1
                    while(l<r and nums[r-1]==nums[r]):
                        r-=1
                    l+=1
                    r-=1
            
            i+=1
                    
        return res
            
            
