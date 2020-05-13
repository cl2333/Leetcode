class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            self.search_pair(nums, -nums[i], i+1, result)
        return result
    
    def search_pair(self, arr, target_sum, left, triplets):
        right = len(arr)-1
        while left < right:
            if arr[left] + arr[right] == target_sum:
                print(left, right, target_sum, arr[left], arr[right] )
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
            
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            
            elif arr[left] + arr[right] > target_sum:
                right -= 1
            else:
                left += 1
        
    
                        