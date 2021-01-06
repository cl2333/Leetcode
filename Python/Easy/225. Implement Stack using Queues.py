from collections import deque 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque([])
        self.queue2 = deque([])
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.queue1) - 1):
            val = self.queue1.popleft()
            self.queue2.append(val)
        
        val = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val
        

    def top(self) -> int:
        """
        Get the top element.
        """
        val = self.pop()
        self.push(val)
        return val
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()