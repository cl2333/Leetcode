# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        last_end = None
        begin = head
        
        
        while begin:
            end = begin.next
            if end:
                next_begin = end.next
            else:
                break
                
            end.next = begin
            begin.next = next_begin
            
            if not last_end:
                head = end
            else:
                last_end.next = end
            
            last_end = begin
            begin = next_begin
         
            
        return head


def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next