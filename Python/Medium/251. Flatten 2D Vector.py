from collections import deque
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = deque(v)

    def next(self) -> int:
        tmp_list = self.v.popleft()
        while len(tmp_list) == 0:
            tmp_list = self.v.popleft()
        value = tmp_list[0]
        if len(tmp_list) > 1:
            self.v.appendleft(tmp_list[1:])
        return value
        

    def hasNext(self) -> bool:
        return sum(len(i) > 0 for i in self.v)  > 0
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class Vector2D:
    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.vec = vec2d
        
    # @return {integer}
    def next(self):
        if self.hasNext():
            result = self.vec[self.row][self.col]
            self.col += 1
            return result

    # @return {boolean}
    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            
            self.col = 0
            self.row += 1
            
        return False