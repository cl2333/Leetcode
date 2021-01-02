class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abb_count = {}
        for word in dictionary:
            if len(word) == 1:
                abb = word
            else:
                abb = word[0] + str(len(word[1:-1])) + word[-1]
            self.abb_count[abb] = self.abb_count.setdefault(abb, [])
            if word not in self.abb_count[abb]:
                self.abb_count[abb].append(word)

    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            abb = word
        else:
            abb = word[0] + str(len(word[1:-1])) + word[-1]
         
        if abb not in self.abb_count or self.abb_count[abb] == [word]:
            return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)