# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(root,d):
    if root==None:
        return d;
    else:
        return max(depth(root.left,d+1),depth(root.right,d+1))
class Solution(object):
    def maxDepth(self, root):
        return depth(root,0)
        
