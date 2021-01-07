# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []
        self.recursive(root, result, [str(root.val)])
        return result
        
    
    def recursive(self, root, result, cur):
        if not root.left and not root.right:
            result.append("->".join(cur))
         
        if root.left:
            cur.append(str(root.left.val))
            self.recursive(root.left, result, cur)
            cur.pop()
        
        if root.right:
            cur.append(str(root.right.val))
            self.recursive(root.right, result, cur)
            cur.pop()
        