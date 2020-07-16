# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        start = head
        length = 0
        while start:
            start = start.next
            length += 1
            
        k = k%length
        
        if k == 0:
            return head
        end = head
        
        for i in range(length-k-1):
            end = end.next

        start = end.next
        end.next = None
        connect = start
      
        while connect.next:
            connect = connect.next
        
        connect.next = head
        return start
            
        