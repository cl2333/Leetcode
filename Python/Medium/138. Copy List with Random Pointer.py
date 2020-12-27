"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        cur_new = dummy
        cur = head
        dct = {}
        dct[None] = None   
        
        while cur:
            cur_new.next = Node(cur.val)
            cur_new = cur_new.next
            dct[cur] = cur_new
            cur = cur.next
        cur_new.next = None
        
        cur_new = dummy.next
        cur = head
        while cur:
            cur_new.random = dct[cur.random]
            cur = cur.next
            cur_new = cur_new.next
        
        return dummy.next
            
        
        
            
        