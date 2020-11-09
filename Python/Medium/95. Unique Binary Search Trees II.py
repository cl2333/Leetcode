# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        else:
            return self.find(1,n)
    
    def find(self, left, right):
        if left > right:
            return [None]
        
        result = []
        
        for i in range(left, right+1):
            left_nodes = self.find(left, i-1)
            right_nodes = self.find(i+1, right)
            for l in left_nodes:
                for r in right_nodes:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        
        return result
