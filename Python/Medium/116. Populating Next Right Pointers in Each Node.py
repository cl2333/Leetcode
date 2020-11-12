"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        tmp = deque([root])
        
        while tmp:
            n = len(tmp)
            for i in range(n):
                cur = tmp.popleft()
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
                if i == n-1:
                    cur.next = None
                else:
                    cur.next = tmp[0]
                
        return root
            

        