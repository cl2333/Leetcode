"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        root.next = None
        tmp = root
        while tmp and tmp.left:
            node = tmp
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                else:
                    node.right.next = None
                node = node.next
            
            tmp = tmp.left
                      
        return root
            

        