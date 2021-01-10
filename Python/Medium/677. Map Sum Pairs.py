class TrieNode:
    
    def __init__(self):
        self.next = {}
        self.sum = {}
        self.words = set()
        

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
            
            if key not in node.words:
                node.sum[key] = val
                node.words.add(key)
            else:
                node.sum[key] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.next:
                return 0
            node = node.next[c]
        return sum(node.sum.values())
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)