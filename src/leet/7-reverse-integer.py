# coding: utf8
"""
---------------------------------------------
    File Name: 7-reverse-integer
    Description: 
    Author: wangdawei
    date:   2018/4/23
---------------------------------------------
    Change Activity: 
                    2018/4/23
---------------------------------------------    
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        if x<0:
            res = -int(str(x)[1:][::-1])
        else:
            res = int(str(x)[::-1])

        if -2**31<= res <= 2**31-1:
            return res
        else:
            return 0

solu = Solution()
assert solu.reverse(123) == 321
assert solu.reverse(120) == 21
assert solu.reverse(-12) == -21


