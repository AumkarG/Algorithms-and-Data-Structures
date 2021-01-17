def traverse(root,mn):
    if(root):
        if(root.val>mn):
            return root.val
        else:
            l=traverse(root.left,mn)
            r=traverse(root.right,mn)
            if(l):
                if(r):
                    return min(l,r)
                else:
                    return l
            else:
                return r
            
class Solution(object):
    def findSecondMinimumValue(self, root):
        mn=root.val
        x=traverse(root,mn)
        if(x):
            return x
        else:
            return -1
        
        
