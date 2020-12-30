class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                if nums[-nums[i] - 1] < 0:
                    return -nums[i]
                else:
                    nums[-nums[i] - 1] = - nums[-nums[i] - 1]
            else:
                if nums[nums[i] - 1] < 0:
                    return nums[i]
                else:
                    nums[nums[i] - 1] = - nums[nums[i] - 1]
        
    

    def findDuplicate(self, nums):
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder