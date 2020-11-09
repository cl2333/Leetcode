# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        
        return res[::-1]