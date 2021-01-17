def inorder(root,x):
    if(root.left):
        inorder(root.left,x)
    x.append(root.val)
    if(root.right):
        inorder(root.right,x)
        
class Solution(object):
    def isValidBST(self, root):
        if(root is None):
            return True
        x=[]
        inorder(root,x)
        for i in range(len(x)-1):
            if(x[i]>=x[i+1]):
                return False
        return True
            
        
