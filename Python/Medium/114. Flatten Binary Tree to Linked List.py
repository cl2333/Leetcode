# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_and_find_last(root)
    
    def flatten_and_find_last(self, root):
        if root is None:
            return None
        
        left_last = self.flatten_and_find_last(root.left)
        right_last = self.flatten_and_find_last(root.right)
        
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        return right_last or left_last or root