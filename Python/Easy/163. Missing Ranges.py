class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        
        
        nums.append(upper + 1)
        pre = lower - 1
        
        result = []
        for i in range(len(nums)):
            if nums[i] == pre + 2:
                result.append(str(pre + 1))
            elif nums[i] > pre + 2:
                result.append(str(pre + 1) + "->" + str(nums[i] - 1))

            pre = nums[i]
        
        return result
            
                