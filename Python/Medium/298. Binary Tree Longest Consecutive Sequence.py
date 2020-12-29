# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.backtrack(root)[-1]
        
    def backtrack(self, root):
        if not root:
            return (0, None, 0)
        
        max_len, root_len = 1, 1
        left_len, left_val, max_left = self.backtrack(root.left)
        right_len, right_val, max_right = self.backtrack(root.right)
        
        
        if left_val != None and root.val + 1 == left_val:
            root_len = max(root_len, left_len + 1)
        if right_val != None and root.val + 1 == right_val:
            root_len = max(root_len, right_len + 1)
        
        max_len = max(root_len, max_left, max_right)
        
        return (root_len, root.val, max_len)
        