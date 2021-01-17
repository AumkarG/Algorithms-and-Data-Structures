class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count=[0]*101
        for i in nums:
            count[i]+=1
        prev=count[0]
        count[0]=0
        for i in range(1,101):
            temp=count[i]
            count[i]=count[i-1]+prev
            prev=temp
        res=[]
        for i in nums:
            res.append(count[i])
        return res
