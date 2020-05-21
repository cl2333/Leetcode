class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]  < nums[i]:
                index = i-1
                break
        
        
        if index == -1:
            nums.sort()
        else:    
            min_index = index+1
            min_value = nums[index+1]

            for i in range(min_index,len(nums)):
                if nums[i] > nums[index] and nums[i] < min_value:
                    min_value = nums[i]
                    min_index = i

            nums[index], nums[min_index] = nums[min_index], nums[index]

            nums[index+1:]= sorted(nums[index+1:])
        
                
           
def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1