# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tmp = deque([root])
        result = []
        index = 1
        
        while tmp:
            cur_res = []
            for i in range(len(tmp)):
                root = tmp.popleft()
                cur_res.append(root.val)
                
                if root.left:
                    tmp.append(root.left)
                if root.right:
                    tmp.append(root.right)
            
            if index == 1:
                result.append(cur_res)
            else:
                result.append(cur_res[::-1])
            
            index *= -1
            
        return result
        
        