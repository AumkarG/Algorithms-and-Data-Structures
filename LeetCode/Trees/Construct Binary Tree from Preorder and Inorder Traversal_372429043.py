# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
def construct(pre,ino):
    if(pre):
        root=TreeNode(pre[0],None,None)
        i=0
        while i < len(ino):
            if(ino[i]==root.val):
                break
            i+=1
            
        root.left=construct(pre[1:i+1],ino[0:i])
        root.right=construct(pre[i+1:],ino[i+1:])
        return root

class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
