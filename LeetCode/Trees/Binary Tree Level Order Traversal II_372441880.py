# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        final=[]
        q=[root]
        while(q):
            curr=[]
            for i in range(len(q)):
                x=q.pop(0)
                curr.append(x.val)
                if(x.left):
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
            final.append(curr)
        return final[::-1]
                
