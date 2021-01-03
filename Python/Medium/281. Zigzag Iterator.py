class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0

    def next(self) -> int:
        if self.index1 <= self.index2 and self.index1 < len(self.v1):
            self.index1 += 1
            return self.v1[self.index1 - 1]
        if self.index1 > self.index2 and self.index2 < len(self.v2):
            self.index2 += 1
            return self.v2[self.index2 - 1]
        if self.index1 <= self.index2 and self.index2 < len(self.v2):
            self.index2 += 1
            return self.v2[self.index2 - 1]
        if self.index1 > self.index2 and self.index1 < len(self.v1):
            self.index1 += 1
            return self.v1[self.index1 - 1]

    def hasNext(self) -> bool:
        return self.index1 < len(self.v1) or self.index2 < len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())