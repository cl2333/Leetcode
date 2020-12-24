# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            if head.val < head.next.val:
                head = head.next
            else:
                pre = dummy
                insert = head.next
                while pre.next.val < insert.val:
                    pre = pre.next
                
                insert_next= insert.next
                pre_next = pre.next
                
                pre.next = insert
                insert.next = pre_next
                head.next = insert_next
                
        return dummy.next
                
        