# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if ( p and not q ) or (q and not p):
            return False
        if p.val != q.val:
            return False
         
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        