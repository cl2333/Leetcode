class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.stream=[]
        self.size=size

    def next(self, val: int) -> float:
        self.stream.append(val)
        if len(self.stream) >self.size:
            return sum(self.stream[-self.size:])/self.size
        else:
            return sum(self.stream)/len(self.stream)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

#using collections.deque
import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)