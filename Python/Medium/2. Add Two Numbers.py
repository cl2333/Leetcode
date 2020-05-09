# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = 0,0
        cnt1, cnt2 = 0,0
        while l1 is not None:
            list1=list1+l1.val*(10**cnt1)
            cnt1 += 1
            l1 = l1.next
            
        while l2 is not None:
            list2=list2+l2.val*(10**cnt2)
            cnt2 += 1
            l2 = l2.next
        
        n = list1+list2
    
        result=temp=None
        if n == 0:
            return ListNode()
        
        while n >0:
            remain = n%10
            n = n//10
            node = ListNode(remain)
            if temp is not None:
                temp.next = node
            temp = node
            if result is None:
                result = node
                
        return result
                
                
        
    