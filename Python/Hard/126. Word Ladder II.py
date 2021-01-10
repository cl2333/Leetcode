from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)
        chars = set([c for word in wordList for c in word])
        
        result = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            new_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    result.extend(i for i in layer[word])
                else:
                    for i in range(len(word)):
                        for c in chars:
                            n_word = word[:i] + c + word[i + 1:]
                            if n_word in wordList:
                                new_layer[n_word] += [prev + [n_word] for prev in layer[word]]
                
            wordList -= set(new_layer.keys())
            layer = new_layer
        
        return result
        
        