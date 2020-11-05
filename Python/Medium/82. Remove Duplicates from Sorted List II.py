# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l1 = h1 = ListNode(0)
        l1.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                
                head = head.next
                l1.next = head
            else:
                head = head.next
                l1 = l1.next
        
        return h1.next
        
        