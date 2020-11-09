# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tmp = deque([root])
        res = []
        while tmp:
            cur_res = []
            for i in range(len(tmp)):
                cur = tmp.popleft()
                cur_res.append(cur.val)
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            res.append(cur_res)
        
        return res

# def levelOrder(self, root):
#     ans, level = [], [root]
#     while root and level:
#         ans.append([node.val for node in level])            
#         level = [kid for n in level for kid in (n.left, n.right) if kid]
#     return ans
            
        