# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            return self.delete(root)
        node = root
        dummy = TreeNode(0)
        while node:
            if node.val > key:
                dummy = node
                node = node.left
            elif node.val < key:
                dummy = node
                node = node.right
            else:
                break

        if not node or node.val != key:
            return root
        
        if dummy.left == node:
            dummy.left = self.delete(node)
        else:
            dummy.right = self.delete(node)
        return root
        
        
    def delete(self, node):
        if not node.left and not node.right:
            return None
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        
        root = node
        node = node.left
        if not node.right:
            node.right = root.right
            return node
        
        while node.right:
            tmp = node
            node = node.right

        tmp.right = node.left
        node.right = root.right
        node.left = root.left
        return node
        
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        
        # we always want to delete the node when it is the root of a subtree,
        # so we handle left or right according to the val.
        # if the node does not exist, we will hit the very first if statement and return None.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # now the key is the root of a subtree
        else:
            # if the subtree does not have a left child, we just return its right child
            # to its father, and they will be connected on the higher level recursion.
            if not root.left:
                return root.right
            
            # if it has a left child, we want to find the max val on the left subtree to 
            # replace the node we want to delete.
            else:
                # try to find the max value on the left subtree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                    
                # replace
                root.val = tmp.val
                
                # since we have replaced the node we want to delete with the tmp, now we don't
                # want to keep the tmp on this tree, so we just use our function to delete it.
                # pass the val of tmp to the left subtree and repeat the whole approach.
                root.left = self.deleteNode(root.left, tmp.val)
        
        return root        
        
        
            

                
                
        
        
        
        