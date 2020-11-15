from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        chars = list(set([i  for word in wordList for i in word ]))
        queue = deque([(beginWord, 1)])
        
        while queue:
            beginWord, level = queue.popleft()
            if beginWord == endWord:
                return level
            
            for i in range(len(beginWord)):
                for j in chars:
                    cur = beginWord[:i] + j + beginWord[i+1:]
                    if cur in wordList:
                        wordList.remove(cur)
                        queue.append((cur, level+1))
                    
        return 0

