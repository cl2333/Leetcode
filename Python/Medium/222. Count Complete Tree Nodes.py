# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
        
#         queue = deque([root])
#         count = 0
#         while queue:
#             count += len(queue)
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
                    
#         return count
        if not root:
            return 0
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        
        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            return 2 ** right_depth + self.countNodes(root.left)
        

    def depth(self, root):
        if not root:
            return 0
        return 1 + self.depth(root.left)
        
        