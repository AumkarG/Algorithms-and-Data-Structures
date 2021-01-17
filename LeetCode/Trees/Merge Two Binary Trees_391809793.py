# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def merge(t1,t2,t3):
    if (t1) and (t2):
        t3.val=t1.val+t2.val  
        if(t1.left or t2.left):
            t3.left=TreeNode()
            merge(t1.left,t2.left,t3.left)
        if(t1.right or t2.right):
            t3.right=TreeNode()
            merge(t1.right,t2.right,t3.right)
    elif t1:
        t3.val=t1.val
        t3.left=t1.left
        t3.right=t1.right
    elif t2:
        t3.val=t2.val
        t3.left=t2.left
        t3.right=t2.right
        
    
class Solution(object):
    def mergeTrees(self, t1, t2):
        if(t1 or t2):
            t3=TreeNode()
            merge(t1,t2,t3)
            return t3
        else:
            return None
