# coding: utf8
"""
---------------------------------------------
    File Name: 8-string-to-integer-atoi
    Description: 
    Author: wangdawei
    date:   2018/4/23
---------------------------------------------
    Change Activity: 
                    2018/4/23
---------------------------------------------    
"""

import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strList = re.findall(r"^\s*([\+\-]?[0-9]+)", str)
        if len(strList) == 0:
            return 0

        res = int(strList[0])
        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        elif res > 2 ** 31 - 1:
            return 2147483647
        else:
            return -2147483648


solu = Solution()
assert solu.myAtoi("  -42abc") == -42
assert solu.myAtoi("  +42abc") == 42
assert solu.myAtoi(" -91283472332abc ") == -2147483648
assert solu.myAtoi("2147483648") == 2147483647