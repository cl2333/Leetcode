class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        current_word, current_index = None, 0
        result = len(words)
        for i, word in enumerate(words):
            if word != word1 and word != word2:
                continue
            if current_word and word != current_word:
                result = min(result, i - current_index)
            elif current_word and word1 == word2:
                result = min(result, i - current_index)
            current_word, current_index = word, i
        
        return result
                
                