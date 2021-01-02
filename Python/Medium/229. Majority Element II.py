from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
#         counter = Counter(nums)
#         result = []
        
#         for key, value in counter.items():
#             if value > len(nums) // 3:
#                 result.append(key)
        
#         return result
        
        if not nums:
            return []
        
        count1, count2, num1, num2 = 0, 0, 0, 1
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1 = num
                count1 = 1
            elif count2 == 0:
                num2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [i for i in (num1, num2) if nums.count(i) > len(nums) // 3]
        