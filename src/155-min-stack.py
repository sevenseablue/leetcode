#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minstack and x < self.minstack[-1][1]:
            self.minstack.append((len(self.stack)-1, x))
        elif not self.minstack:
            self.minstack.append((0, x))

    def pop(self):
        """
        :rtype: void
        """
        ele = self.stack.pop()
        if len(self.stack) == self.minstack[-1][0]:
            self.minstack.pop()
        return ele

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)

# param_3 = obj.top()
# param_4 = obj.getMin()
print(obj.getMin())
# print(obj.getMin())
print(obj.pop())
# print(obj.getMin())
print(obj.top())
print(obj.getMin())

