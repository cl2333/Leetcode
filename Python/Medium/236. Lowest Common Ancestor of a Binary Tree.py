# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        is_p, is_q, node = self.find_lowest(root, p, q)
        
        if is_p and is_q:
            return node
        return None
    
    def find_lowest(self, root, p, q):
        if root is None:
            return False, False, None
        
        left_p, left_q, left_node = self.find_lowest(root.left, p, q)
        right_p, right_q, right_node = self.find_lowest(root.right, p, q)
        
        is_p =  left_p or right_p or root == p
        is_q =  left_q or right_q or root == q
        
        if root == p or root == q:
            return is_p, is_q, root
        
        if left_node and right_node:
            return is_p, is_q, root
        if left_node:
            return is_p, is_q, left_node
        if right_node:
            return is_p, is_q, right_node
        
        return is_p, is_q, None
        