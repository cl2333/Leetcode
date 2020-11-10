# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        left, right = 0, len(nums)-1
        mid = (left+right) // 2
        
        root = TreeNode(nums[mid])
        left_node = self.sortedArrayToBST(nums[:mid])
        right_node = self.sortedArrayToBST(nums[mid+1:])
        root.left = left_node
        root.right = right_node
        
        return root
        