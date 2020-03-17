class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = []
        for c in S:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        
        return "".join(ans)