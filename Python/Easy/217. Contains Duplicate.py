class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i=0
        if len(nums)<=1:
            return False
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
                break
        return False
        