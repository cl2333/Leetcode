# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return head
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        reverse = self.reverseList(mid)
        return self.merge(head, reverse)
        
    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        return prev
    
    def merge(self, head, reverse):
        l1 = head
        l2 = reverse
        while l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
   
        return head
            
            
           
    