# coding: utf8
"""
---------------------------------------------
    File Name: Ugly Number II
    Description: 
    Author: wangdawei
    date:   2018/2/1
---------------------------------------------
    Change Activity: 
                    2018/2/1
---------------------------------------------    
"""

from heapq import heappush, heappop

class Solution:

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        heapset = set([1])
        ugly = []
        factors = [2, 3, 5]
        for i in range(n):
            u = heappop(heap)
            ugly.append(u)
            neweles = [e*u for e in factors]
            for e in neweles:
                if e not in heapset:
                    heapset.add(e)
                    heappush(heap, e)
        return ugly[n-1]


solu = Solution()
for i in range(1, 11):
    print(solu.nthUglyNumber(i))