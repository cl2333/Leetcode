class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append((x,min(self.getMin(),x)))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if not self.q:
            return None
        else:
            return self.q[-1][0]

    def getMin(self) -> int:
        if self.q:
            return self.q[-1][1]
        return inf


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()