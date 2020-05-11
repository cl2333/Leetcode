class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_x = x
        if x < 0:
            return False
        remain = 0
        count = 0
        while x >0:
            remain = (x%10)+(remain*10)
            count += 1
            x //= 10
        if remain == input_x:
            return True
        return False
        