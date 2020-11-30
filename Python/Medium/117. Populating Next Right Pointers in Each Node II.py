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
        
        cur = dummy = Node(0)
        node = root
        while node:
            cur.next = node.left
            if cur.next:
                cur = cur.next
            cur.next = node.right
            if cur.next:
                cur = cur.next
            node = node.next
            
            if not node:
                node = dummy.next
                cur = dummy
        
        return root

        
            
        