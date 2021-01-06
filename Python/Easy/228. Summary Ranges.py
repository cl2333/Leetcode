class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        lower, pre = nums[0], nums[0]
        result = []
        
        for i in range(1, len(nums)):
            if nums[i] != pre + 1:
                if lower == pre:
                    result.append(str(pre))
                else:
                    result.append(str(lower) + "->" + str(pre))
                lower, pre = nums[i], nums[i]
            else:
                pre += 1
        
        if lower == pre:
            result.append(str(pre))
        else:
            result.append(str(lower) + "->" + str(pre))
        
        return result
            
            