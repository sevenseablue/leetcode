#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""

from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.que1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            raise Exception("pop a empty stack")
        while self.que1:
            ele = self.que1.popleft()
            if self.que1:
                self.que2.append(ele)
        self.que1 = self.que2
        self.que2 = deque()
        return ele

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            raise Exception("pop a empty stack")
        while self.que1:
            ele = self.que1.popleft()
            self.que2.append(ele)
        self.que1 = self.que2
        self.que2 = deque()
        return ele

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.que1) == 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2,param_3,param_4)
