# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def delete(root,to_delete,li): 
        if(root==None):
            return False
        elif(root.val in to_delete):
            if(root.left is not None):
                delete(root.left,to_delete,li)
                if(root.left.val not in to_delete):
                    li.append(root.left)
            if(root.right is not None):
                delete(root.right,to_delete,li)
                if(root.right.val not in to_delete):
                    li.append(root.right)
            return True
        else:
            if(delete(root.left,to_delete,li)):
                root.left=None
            if(delete(root.right,to_delete,li)):
                root.right=None
            return False
        
class Solution:
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        li = []

        if(root==None):
            return 
        elif(root.val in to_delete):
            if(root.left is not None and root.left.val not in to_delete):
                li.append(root.left)
            if(root.right is not None and root.right.val not in to_delete):
                li.append(root.right)
            delete(root.left,to_delete,li)
            delete(root.right,to_delete,li)

        else:
            li.append(root)
            delete(root,to_delete,li)
        
        return li

            
            
                

            
