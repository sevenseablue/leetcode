# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-23 下午10:39'
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        d = [1] * (n+1)
        for i in range(1, n+1):
            res = 0
            for j in range(1, i+1):
                res += d[j-1]*d[i-j]
            d[i] = res

        return d[n]

solu = Solution()
for i in range(5):
    print(solu.numTrees(i))

