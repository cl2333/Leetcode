# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.find(root, sum, [], res)
        return res
    
    def find(self, root, sum, cur, result):
        if not root:
            return 
        if root.val == sum and not root.left and not root.right:
            result.append(cur+[root.val])
            
        self.find(root.left, sum - root.val, cur+[root.val], result) or self.find(root.right, sum - root.val, cur+[root.val], result)