class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l + r) //2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    
            return l
                
        
#one-line solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        return len([x for x in nums if x<target])