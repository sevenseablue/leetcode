# coding: utf8
"""
---------------------------------------------
    File Name: 699-falling-squares
    Description: 
    Author: wangdawei
    date:   2018/5/7
---------------------------------------------
    Change Activity: 
                    2018/5/7
---------------------------------------------    
"""

import bisect

class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        lines = []
        result = 0
        heights = []
        for xl, sidelen in positions:
            xr = xl + sidelen - 1
            li = bisect.bisect(lines, (xl-0.1, 0, 0))
            ri = bisect.bisect(lines, (xr+0.1, 0, 0))
            h_max = 0
            for i in range(li, ri + 1):
                h_max = max(h_max, lines[i][1])
            for tl, tr, th in heights:
                if tl < xl and tr > xr:
                    h_max = max(h_max, th)
            if 0<=li<len(lines) and xl != lines[li][0]:
                lines.insert(li, (xl, h_max))
            else:
                lines[li] = (xl, h_max)
            if xr != lines[ri][0]:
                pass
            # lines.insert()






