# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head.next.next
        
        
        loop = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop = True
                break
        
        if not loop:
            return None
        
        count = 1
        slow = slow.next
        fast = fast.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
            count += 1
        
        fast = slow = head
        while count > 0:
            fast = fast.next
            count -= 1
        
        pos = 0
        while fast != slow:
            slow = slow.next
            fast = fast.next
            pos += 1
        
        return slow
        

#better solution
def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head