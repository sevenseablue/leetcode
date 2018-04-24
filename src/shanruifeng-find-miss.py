# coding: utf8
"""
---------------------------------------------
    File Name: shanruifeng-find-miss
    Description: 
    Author: wangdawei
    date:   2018/4/24
---------------------------------------------
    Change Activity: 
                    2018/4/24
---------------------------------------------    
"""

class Solution:
    def findMiss(self, arr):
        l, r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)>>1
            if mid == 0:
                return arr[0] + 1
            if arr[mid] != arr[mid-1]+1:
                return arr[mid-1] + 1
            elif arr[mid]>arr[0]+mid:
                r = mid-1
            else:
                l = mid+1


solu = Solution()
for arr in [[0, 2],
            [0, 1, 3],
            [0, 2, 3],
            [0, 1, 2, 4],
            [0, 1, 3, 4],
            [0, 2, 3, 4],
            [0, 1, 2, 3, 5],
            [0, 1, 2, 4, 5],
            [0, 1, 3, 4, 5],
            [0, 2, 3, 4, 5],
            ]:
    print(solu.findMiss(arr))
