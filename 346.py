import math
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window=[]
        for i in range(size):
            self.window.append(None)
        print(self.window)
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.pop(0)
        self.window.append(val)
        divenden=len(self.window)
        sum1=0
        for v in self.window:
            if v == None:
                divenden -=1
                continue
            sum1+=v
        return (sum1/divenden)
        


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))