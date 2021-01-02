# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        succ = None
        node = root
        while node:
            if p.val < node.val:
                succ = node
                node = node.left
            else:
                node = node.right
                
        return succ