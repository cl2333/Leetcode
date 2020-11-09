# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode, max_val = float('inf'), min_val = float('-inf')) -> bool:

        if not root:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            return False

        return self.isValidBST(root.left, min(max_val, root.val), min_val) and self.isValidBST(root.right, max_val, max(min_val, root.val))