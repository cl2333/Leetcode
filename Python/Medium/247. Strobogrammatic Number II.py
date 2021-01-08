class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.dct = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        if n == 1:
            return ["0", "1", "8"]
        
        half = []
        result = []
        length = (n - 2) // 2
        self.recursive(length, "", half)
        for char in ["1", "6", "8", "9"]:
            if n % 2 == 0:
                for string in half:
                    result.append(char + string + self.getRotate(string) + self.dct[char])
            if n % 2 == 1:
                for mid in ["0", "1", "8"]:
                    for string in half:
                        result.append(char + string + mid + self.getRotate(string) + self.dct[char])
        
        return result
    
    
    def recursive(self, n, cur, half):
        if len(cur) == n:
            half.append(cur)
            return
        
        for i in range(len(self.dct.values())):
            self.recursive(n, cur + list(self.dct.values())[i], half)
        
    def getRotate(self, string):
        result = ""
        for s in string:
            result = self.dct[s] + result
        return result

    def findStrobogrammatic(self, n):
        evenMidCandidate = ["11","69","88","96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else: 
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = (n-1)/2
        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]