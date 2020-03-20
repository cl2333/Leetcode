class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums=[0] + nums
        for num in nums:
            if nums[abs(num)]>0:
                nums[abs(num)]=-nums[abs(num)]
        
        return [i for i in range(1,len(nums)) if nums[i]>0]
            
                
        #return set(range(1,len(nums)+1))-set(nums)
               
        