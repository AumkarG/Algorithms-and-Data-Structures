def inorder(root,x,k):
    if(root is not None):
        inorder(root.left,x,k)
        x.append(root.val)
        if(len(x)<k):
            inorder(root.right,x,k)
class Solution(object):
    def kthSmallest(self, root, k):
        x=[]
        inorder(root,x,k)
        return x[k-1]
        
        
