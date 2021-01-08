class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        index1 = [i for i in range(len(words)) if words[i] == word1]
        index2 = [i for i in range(len(words)) if words[i] == word2]
        
        ans = float('inf')
        for i1 in index1:
            for i2 in index2:
                ans = min(ans, abs(i1 - i2))
                
        return ans


    def shortestDistance(self, words, word1, word2):
        ans = len(words)
        current_word, current_index = None, 0
        for index, word in enumerate(words):
            if word != word1 and word != word2: 
                continue
            if current_word and word != current_word:
                ans = min(ans, index - current_index)
            current_word, current_index = word, index
        return ans