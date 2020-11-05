class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = len(nums1)-1
        
        l1, l2 = m-1, n-1
        
        while l1 >= 0 and l2>=0 :
            if nums1[l1] <= nums2[l2]:
                nums1[index] = nums2[l2]
                l2 -= 1
                index -= 1
            
            else:
                nums1[index] = nums1[l1]
                l1 -= 1
                index -= 1 
                
                
        if l2 >= 0:
            nums1[:l2+1] = nums2[:l2+1]