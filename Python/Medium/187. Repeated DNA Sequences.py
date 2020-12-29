class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        word_set = set()
        result = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] not in word_set:
                word_set.add(s[i:i + 10])
            else:
                result.add(s[i:i + 10])
        
        return list(result)
        