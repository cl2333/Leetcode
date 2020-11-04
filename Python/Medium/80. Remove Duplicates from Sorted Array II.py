class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <=2 :
            return len(nums)
        
        former, latter = 1, 1 
        count = 1
        
        while latter < len(nums):
            if nums[latter] == nums[latter-1]:
                count += 1
            else:
                count = 1
                
            nums[former] = nums[latter]
            
            if count <= 2:
                former += 1
                latter += 1
            else:
                latter += 1
        
        return former
            
            
            