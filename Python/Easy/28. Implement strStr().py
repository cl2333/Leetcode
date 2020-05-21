class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle)==0:
        #     return 0
        # return haystack.find(needle)
        
        if len(needle) > len(haystack) :
            return -1
        if not needle:
            return 0
        
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
        