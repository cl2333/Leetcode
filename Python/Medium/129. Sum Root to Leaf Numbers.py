# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        self.find(root, result, 0)
        return sum(result)
    
    
    def find(self, root, res, cur):
        if not root.left and not root.right:
            res.append(cur*10+root.val)
            return 
        
        if  root.left and  root.right:
            self.find(root.left, res, cur*10 + root.val) or self.find(root.right, res, cur*10 + root.val)
        if  root.left and not root.right:
            self.find(root.left, res, cur*10 + root.val)
        if not root.left and  root.right:
            self.find(root.right, res, cur*10 + root.val)
