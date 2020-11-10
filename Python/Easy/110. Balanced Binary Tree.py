# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

# class Solution(object):
#     def isBalanced(self, root):
            
#         def check(root):
#             if root is None:
#                 return 0
#             left  = check(root.left)
#             right = check(root.right)
#             if left == -1 or right == -1 or abs(left - right) > 1:
#                 return -1
#             return 1 + max(left, right)
            
#         return check(root) != -1
        
    def depth(self, root):
        if not root:
            return 0
        return 1+max(self.depth(root.left), self.depth(root.right))