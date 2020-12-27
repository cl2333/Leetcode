# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:
            return root
        
        queue = []
        node = root
        while node and node.left:
            queue.append(node)
            node = node.left
            
        new_root = node
        while queue:
            new_right = queue.pop()
            new_left = new_right.right
            new_right.right = None
            new_right.left = None
            node.left = new_left
            node.right = new_right
            node = new_right
        
        return new_root
        
        