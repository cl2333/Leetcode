# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.ans=0
        
        def depth(n):
            if not n:
                return 0
            left=depth(n.left)
            right=depth(n.right)
            self.ans=max(self.ans,left+right)
            return 1+max(left,right)
       
        depth(root)
        
        return self.ans
        