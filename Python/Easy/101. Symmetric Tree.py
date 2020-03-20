# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
    
        def Symmetric(p,q):
            if not p and not q:
                return True
            if p and q and p.val==q.val:
                return Symmetric(p.left,q.right) and Symmetric(p.right,q.left)
            return False
            
        
        return not root or Symmetric(root.left,root.right)
        
        #using stack

        queue=[]
        
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif root.left and root.right and root.left.val==root.right.val:
            queue.append(root.left)
            queue.append(root.right)
        else:
            return False
        
        flag=True
        while queue:
            right=queue.pop()
            left=queue.pop()
            
            if not left.left and not right.right:
                flag=True
            elif left.left and right.right and left.left.val==right.right.val:
                queue.append(left.left)
                queue.append(right.right)
            else:
                return False
            
            if not left.right and not right.left:
                flag=True
            elif left.right and right.left and right.left.val==left.right.val:
                queue.append(left.right)
                queue.append(right.left)
            else:
                return False
            
        return flag