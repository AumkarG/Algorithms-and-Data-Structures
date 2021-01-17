def bin(target, arr,l,r):
    mid=(r+l)/2

    if(r>l):
        if(arr[mid]==target):
            return mid
        else:
            if(arr[mid]>target):
                return bin(target,arr,l,mid)
            else:
                return bin(target,arr,mid+1,r)
    else:
        if(mid>=len(arr)):
            return len(arr)
        if(arr[mid]>target):
            return mid
        else:
            return mid+1
        
class Solution(object):
    def searchInsert(self, nums, target):
        return bin(target, nums,0,len(nums))
