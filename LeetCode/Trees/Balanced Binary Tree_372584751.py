def balance(root):
    if(root is None):
        return (0,True)
    else:
        lv1,l=balance(root.left)
        lv2,r=balance(root.right)
        if(l==False or r==False):
            return -1,False
        m=max(lv1,lv2)
        if(abs(lv1-lv2)<=1):
            x=True
            return (m+1,True)
        else:
            return -1,False
            

class Solution(object):
    def isBalanced(self, root):
        return balance(root)[1]
