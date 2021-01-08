from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque([])
        result = []
        
        for i in range(k):
            while queue:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
                
        for i in range(k, len(nums)):
            result.append(nums[queue[0]])
            
            if i - k + 1 > queue[0]:
                queue.popleft()
            
            while queue:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
        
        
        result.append(nums[queue[0]])
            
        return result
            