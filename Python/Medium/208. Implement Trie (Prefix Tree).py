class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True
    
    
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and node.is_word
    
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#traditional trie

class TrieNode:
    def __init__(self):
        self.next = {}
        self.words: Set[str] = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str):
        self.root.words.add(word)
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode()
            cur = cur.next[c]
            cur.words.add(word)
    
    def search(self, word: str) -> Set[str]:
        cur = self.root
        for c in word:
            if c not in cur.next:
                return set()
            cur = cur.next[c]
        return cur.words