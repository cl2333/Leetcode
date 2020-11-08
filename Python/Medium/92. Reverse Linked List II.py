# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        front = head_node = ListNode(0)
        front.next = head


        
        count = 0
        while front:
            if count == m-1:
                before_m = front

            if count >m and count <=n:
                next_node = front.next
                front.next = before_node
                before_node = front
                front = next_node
                count +=1

            elif count == n+1:
                before_m.next.next = front
                before_m.next = before_node
                return head_node.next     
                
            else:
                before_node = front
                front = front.next
                count += 1
        
        if front == None:
            before_m.next.next = None
            before_m.next.next = front
            before_m.next = before_node
            return head_node.next
        
        return head_node.next


class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next