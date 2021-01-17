def find(root,p,x1):
    if(root==None):
        return False
    elif(root==p):
        x1.append(p)
        return True
    else:
        if(find(root.left,p,x1) or find(root.right,p,x1)):
            x1.append(root)
            return True
        else:
            return False
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x1=[]
        x2=[]
        find(root,p,x1)
        find(root,q,x2)
        l1=len(x1)
        l2=len(x2)
        if(l1<l2):
            s=l1
        else:
            s=l2
        for i in range(0,s):
            if(x1[l1-i-1]!=x2[l2-1-i]):
                return x1[l1-i]
        if s==l1:
            return x1[0]
        else:
            return x2[0]
