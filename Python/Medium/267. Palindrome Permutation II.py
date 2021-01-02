class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        
        mid = [key for key, val in counter.items() if val % 2 == 1]
        if len(mid) > 1:
            return []
        mid = "" if len(mid) == 0 else mid[0]
        half = "".join([key * (val // 2) for key, val in counter.items()])
        half = [i for i in half]
    
        def backtrack(cur):
            if len(cur) == len(half):
                cur = "".join(cur)
                result.append(cur + mid + cur[::-1])
                        
            for i in range(len(half)):
                if visited[i] or ( i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                    continue
                cur.append(half[i])
                visited[i] = True
                backtrack(cur)
                visited[i] = False
                cur.pop()
                
        
        result = []
        visited = len(half) * [False]
        backtrack([])
        return result
        
            