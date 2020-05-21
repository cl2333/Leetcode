class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums)-1
        
        
        
        while start <= end:
            
            mid = (start + end) //2
            print(start,end,mid)
            if nums[mid] == target:
                return mid
            
            if nums[start] <= target:
                if nums[mid] < nums[start]:
                    end = mid -1
                elif nums[mid] > nums[start] and target < nums[mid]:
                    end = mid -1
                else:
                    start = mid+1
            else:
                if nums[mid] >= nums[start]:
                    start = mid + 1
                elif nums[mid] < nums[start] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
                    