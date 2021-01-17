# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if(root):
            q=[root]
            lv=1
            while(q):
                for i in range(len(q)):
                    x=q.pop(0)
                    if(x.left==x.right==None):
                        return lv
                    else:
                        if(x.left):
                            q.append(x.left)
                        if(x.right):
                            q.append(x.right)
                lv+=1
        else:
            return 0
