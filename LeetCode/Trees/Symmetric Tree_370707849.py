# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def ismirror(root1,root2):
    if(root1==root2==None):
        return True
    elif(root1==None):
        return False
    elif(root2==None):
        return False
    return(root1.val==root2.val and ismirror(root1.left,root2.right) and ismirror(root1.right,root2.left))
    
class Solution(object):
    def isSymmetric(self, root):     
        if(root is None):
            return True
        return ismirror(root.left,root.right)
