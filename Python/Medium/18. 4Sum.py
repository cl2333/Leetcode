class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        result = []
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.twoSum(nums, j+1, len(nums)-1, nums[i], nums[j], target, result)
        
        return result
        
    
    def twoSum(self, nums, left, right, first, second, target, result):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target - first - second:
                if (nums[left], nums[right]) != last_pair:
                    result.append([first, second, nums[left], nums[right]])
                    last_pair =  (nums[left], nums[right])     
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target - first - second:
                right -= 1
            else:
                left += 1

                
            
            