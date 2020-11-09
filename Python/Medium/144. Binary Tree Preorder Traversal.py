# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preorder(root, result)
        return result 
    
    def preorder(self, root, result):
        if not root:
            return
        
        result.append(root.val)
        self.preorder(root.left, result)
        self.preorder(root.right, result)
    