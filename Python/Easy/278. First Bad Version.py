# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left, right = 1, n
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        
        if isBadVersion(left):
            return left
        return right
        