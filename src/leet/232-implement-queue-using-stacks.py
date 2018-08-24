#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stackTemp = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.stack:
            self.stackTemp.append(self.stack.pop())
        self.stack.append(x)
        while self.stackTemp:
            self.stack.append(self.stackTemp.pop())


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            return self.stack.pop()
        else:
            raise Exception("pop an empty stack.")

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.stack[-1]
        else:
            raise Exception("peek an empty stack.")

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_4 = obj.empty()
param_2 = obj.pop()


print(param_2, param_3, param_4)
