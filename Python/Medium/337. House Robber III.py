# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.backtrack(root))
        
    def backtrack(self, root):
        if not root:
            return (0, 0)
        
        now, later = 0, 0
        
        left = self.backtrack(root.left)
        right = self.backtrack(root.right)
        
        now = root.val + left[1] + right[1]
        later = max(left) + max(right)
        
        return (now, later)
        
        
        