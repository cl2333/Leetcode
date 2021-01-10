class TrieNode:
    
    def __init__(self):
        self.next = {}
        self.words = set()

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
        
        node.words.add(word)
        
    

class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
            
        res = set()        
        nrows, ncols = len(board), len(board[0])
        
        def dfs(r, c, node):
            if not (0 <= r < nrows and 0 <= c < ncols):
                return 
            
            char = board[r][c]
            if char not in node.next:
                return
            node = node.next[char]
            if node.words:
                res.update(node.words) 
            
            tmp = char
            board[r][c] = "#"
            
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            
            board[r][c] = tmp
            
            
        
        for r in range(nrows):
            for c in range(ncols):
                dfs(r, c, trie.root)
        
        return list(res)