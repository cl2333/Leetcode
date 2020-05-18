class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.search(nums,nums[i],nums[j], target, j+1, result)
        return result
    
    def search(self, nums, value1, value2, target, left, result):
        left = left
        right = len(nums) -1 
        while left < right:
            if nums[left] + nums[right] == target -(value1+value2):
                result.append([value1, value2, nums[left],nums[right]])
                left += 1
                right -= 1
            
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                    
            elif nums[left] + nums[right] >target -(value1+value2):
                right -= 1
            else:
                left += 1
                
            
            