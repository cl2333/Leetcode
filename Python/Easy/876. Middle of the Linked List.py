# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        node = head
        while node:
            node = node.next
            cnt += 1
        cnt = cnt //2 + 1 
        
        node=head
        for i in range(cnt-1):
            node=node.next
        
        return node
    
    # slow and fast pointers
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow