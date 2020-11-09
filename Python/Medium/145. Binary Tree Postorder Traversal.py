# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.postorder(root, result)
        return result 
    
    def postorder(self, root, result):
        if not root:
            return
        
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)
    