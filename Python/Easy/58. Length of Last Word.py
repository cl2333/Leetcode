class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        result = s.strip().split()
        if not result:
            return 0
        return len(result[-1])
        