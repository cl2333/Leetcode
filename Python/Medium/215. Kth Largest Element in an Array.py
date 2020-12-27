class Solution:
    def findKthLargest(self, nums: List[int], n: int) -> int:
        if not nums:
            return -1
        return self.quickSelect(nums, 0, len(nums)-1, len(nums) - n + 1)
    
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        

        left, right = start, end
        pivot = nums[(start + end) //2 ] 
        
        
        while left <= right:
            while left <= right and nums[right] > pivot:
                right -= 1
                
            while left <= right and nums[left] < pivot:
                left += 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1 
                left += 1 
                
                
        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
        elif start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k-(left-start))
        return nums[right+1]
            


        #heap    
        from heapq import *
        result = []
        for num in nums:
            if len(result) < n:
                heappush(result, num)
            else:
                if num > result[0]:
                    heappop(result)
                    heappush(result, num)
        
        return heappop(result)       