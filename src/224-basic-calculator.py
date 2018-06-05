#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""

import re
class Solution:
    def calculatePure(self, arr):
        i = 0
        first = 0
        while i < len(arr):
            if i == 0:
                first = int(arr[0])
                i += 1
            elif arr[i] == "+":
                first += int(arr[i+1])
                i += 2
            elif arr[i] == "-":
                first -= int(arr[i + 1])
                i += 2

        return first

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.replace(" ", "")
        arr = re.split("(\)|\(|\+|\-)", s, flags=True)
        # print(arr)
        stack =  []
        for s in arr:
            if s == "":
                continue
            if s != ")":
                stack.append(s)
            else:
                parenthesis = []
                while stack[-1] != "(":
                    parenthesis.append(stack.pop())

                stack.pop()
                parenthesis.reverse()
                stack.append(self.calculatePure(parenthesis))
        return self.calculatePure(stack)



solu = Solution()
for arr in [["31"],
            ["31", "+", "1", "-", "31"]]:
    print(solu.calculatePure(arr))

for s in ["",
          "(1)",
          "31+1",
          "(31+1)",
          "((31+1))",
          "(31+1+(3+1))",
          "1+3+(31+1)+3+1",
          "(1+(4+5+2)-3)+(6+8)"]:
    print("#"*100)
    print(solu.calculate(s))


