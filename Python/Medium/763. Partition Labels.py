class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dct ={}
        
        for i in range(len(S)):
            c = S[i]
            if c not in dct:
                dct[c] = dct.get(c, [i, i])
            else:
                dct[c][1] = i
        
        schedule = []
        for interval in dct.values():
            schedule.append([interval[0], 1])
            schedule.append([interval[1], 0])
        
        schedule.sort(key = lambda x: x[0])
        output = []
        start, end = 0, 0
        cnt = 0
        for (i, flag) in schedule:
            end = max(end, i)
            if flag == 1:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                output.append(end - start + 1)
                start = end + 1
        
        return output
    



    
    def partition_labels(S):

        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right,rightmost[letter])
        
            if i == right:
                result += [right-left + 1]
                left = i+1

        return result


 class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums) - 1, 0
        
        prev = nums[end]
        for i in range(len(nums)):
            if nums[i] >= prev:
                prev = nums[i]
            else:
                end = i
                
        prev = nums[start]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                start = i
        
        if end != 0:
            return end - start + 1
        
        return 0               