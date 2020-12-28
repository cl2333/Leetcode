class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(self.no_cycle(nums, 0, len(nums)-1), self.no_cycle(nums, 1, len(nums)))
    
    def no_cycle(self, nums, begin, end):
        last, now = 0, 0
        for i in nums[begin:end]:
            last, now = max(last, now), max(now, last + i)
        return now
        