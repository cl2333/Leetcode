# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#        recursive method 
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      
        result = []
        self.front(root, result)
        return result
    
    def front(self, root, result):
        if root == None:
            return
        self.front(root.left, result)
        result.append(root.val)
        self.front(root.right, result)

#use stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:        
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
            
        return result