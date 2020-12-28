class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums) - 1, 0, -1):
            for j in range(len(nums) - 2, len(nums) - i - 2, -1):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        return str(int("".join(map(str, nums))))
                    
                

# bubble sort
def largestNumber2(self, nums):
    for i in xrange(len(nums), 0, -1):
        for j in xrange(i-1):
            if not self.compare(nums[j], nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return str(int("".join(map(str, nums))))
    
def compare(self, n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)