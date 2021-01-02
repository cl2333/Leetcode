class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        self.quickSort(nums, 0, len(nums) - 1)

        mid = len(nums) // 2
        for i in range(1, (len(nums) + 1) // 2 , 2):
            if len(nums) % 2 == 1:
                nums[i], nums[len(nums) - i] = nums[len(nums) - i], nums[i]
            else:
                nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[left + (right - left) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
    
        
    
    def wiggleSort(self, a):
        if not a:
            return
        n = len(a)
        for i in xrange(1, n, 2):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
            
            if i + 1 < n and a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]