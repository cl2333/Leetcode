# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        left, right = float('inf'), float('inf')
        
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)
        
        return 1+min( left, right) 
        