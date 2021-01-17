def sortree(arr):
    if(arr):
        l=len(arr)
        if(l==1):
            return TreeNode(arr[0])
        else:
            x=int(l//2)
            node=TreeNode(arr[x])
            node.left=sortree(arr[0:x])
            node.right=sortree(arr[x+1:])
            return node
    else:
        return None
    
class Solution(object):
    def sortedArrayToBST(self, nums):
        return sortree(nums)
        
