# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=[root]
        j=1
        final=[]
        while(len(q)!=0):
            curr=[]
            for i in range(len(q)):
                x=q.pop(0)
                curr.append(x.val)
                if x.left:
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
            if(j%2==1):
                final.append(curr)
            else:
                final.append(curr[::-1])
            j+=1
        return final
                    
                    
