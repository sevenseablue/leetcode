# coding: utf8
"""
---------------------------------------------
    File Name: Longest Valid Parentheses
    Description: 
    Author: wangdawei
    date:   2018/2/9
---------------------------------------------
    Change Activity: 
                    2018/2/9
---------------------------------------------    
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        long_valid = {}

        for e in s:
            if e == "(":
                stack.append(e)
            else:
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                    long_valid[len(stack)] = long_valid.get(len(stack), 0) + long_valid.get(len(stack)+1, 0) + 1
                    long_valid[len(stack) + 1] = 0
                else:
                    stack.append(")")
        if len(long_valid) == 0:
            return 0
        else:
            return max(long_valid.values())*2


solu = Solution()
for s in ["","(","()",")(",
          ")()())",
          "(()",
          "(()(()",
          "((())()))",
          "((())()))(((())()))",
          "(())"
          ]:
    print(solu.longestValidParentheses(s))


