# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-14 上午10:09'
"""


class Solution:

    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A=sorted(A)
        return self.splitArraySameAverageSorted(A, 0)

solu = Solution()
A=list(range(30))
print(solu.splitArraySameAverage(A))




