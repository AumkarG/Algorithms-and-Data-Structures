# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def construct(post,ino):
    if(ino):
        x=post.pop()
        i=0
        while(i<len(ino)):
            if(ino[i]==x):
                break
            i+=1
        root=TreeNode(x)
        root.left=construct(post[0:i],ino[:i])
        root.right=construct(post[i:],ino[i+1:])
        return root
class Solution(object):
    def buildTree(self, inorder, postorder):
        return construct(postorder,inorder)

