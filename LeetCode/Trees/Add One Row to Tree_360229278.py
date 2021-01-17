

def traverse(root,v,d,dnow):
    if(root):
        if(dnow==d-1):
            node=TreeNode()
            node.val=v
            node.left=root.left
            root.left=node
            node=TreeNode()
            node.val=v
            node.right=root.right
            root.right=node
        else:
            traverse(root.left,v,d,dnow+1)
            traverse(root.right,v,d,dnow+1)

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if(d==1):
            node=TreeNode()
            node.val=v
            node.left=root
            return node
        traverse(root,v,d,1)
        return root
            
        
        
