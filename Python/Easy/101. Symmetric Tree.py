# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.symmetric(root.left, root.right)
    
    def symmetric(self, left, right):
        if not left and not right:
            return True
        elif (not left and right) or (not right and left):
            return False

        elif left.val != right.val:
            return False
        
        res = self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)
        
        return res
            
            
            
        
        