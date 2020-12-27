# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur and cur.next:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            if cur:
                cur = cur.next
        
        return dummy.next