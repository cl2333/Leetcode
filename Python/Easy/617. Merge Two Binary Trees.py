# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            merge=TreeNode(t1.val+t2.val)
            merge.left=self.mergeTrees(t1.left,t2.left)
            merge.right=self.mergeTrees(t1.right,t2.right)
            return merge
        else:
            return t1 or t2
        