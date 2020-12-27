# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        cur = headB
        while cur.next:
            cur = cur.next
        cur.next = headB
        
        slow = fast = headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                begin = headA
                
                while begin != slow:
                    slow = slow.next
                    begin = begin.next
                cur.next = None
                return begin
            
        cur.next  = None   
        return None


# Three rules:

# root's right node becomes the left node of the left node of root
# root becomes the right node of root's left node
# above rules apply on the left edge and return left node along the path.
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right):
            return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return left