# coding: utf8
"""
---------------------------------------------
    File Name: degree of an array
    Description: 
    Author: wangdawei
    date:   2018/1/31
---------------------------------------------
    Change Activity: 
                    2018/1/31
---------------------------------------------    
"""


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        maxd = 0
        maxl = 0
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [i, i, 1]
            else:
                ilist = d[n]
                ilist[1] = i
                ilist[2] += 1
            ilist = d[n]
            l1 = ilist[1] - ilist[0] + 1
            if maxd < ilist[2]:
                maxd = ilist[2]
                maxl = l1
            elif maxd == ilist[2] and maxl > l1:
                maxl = l1

        return maxl


solu = Solution()
for n in [[1,2,2,3,1],
          [1, 2, 2, 3, 1, 4, 2]]:
    print(solu.findShortestSubArray(n))
