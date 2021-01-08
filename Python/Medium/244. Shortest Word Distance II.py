class WordDistance:

    def __init__(self, words: List[str]):
        self.dct, self.length = {}, len(words)
        for i, word in enumerate(words):
            self.dct[word] = self.dct.get(word, []) + [i]

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.dct[word1]
        list2 = self.dct[word2]
        
        ans = self.length
        l1 = l2 = 0
        while l1 < len(list1) and l2 < len(list2):
            ans = min(ans, abs(list1[l1] - list2[l2]))
            if list1[l1] < list2[l2]:
                l1 += 1
            else:
                l2 += 1
        
        return ans
            
            
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)