class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dct = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in dct or dct[num[left]] != num[right]:
                return False
        
            left += 1
            right -= 1
        
        return True