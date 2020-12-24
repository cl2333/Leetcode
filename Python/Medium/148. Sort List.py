# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
        
        
    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy
        
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        
        if left:
            cur.next = left
        if right:
            cur.next = right
        
        return dummy.next
        
        
        