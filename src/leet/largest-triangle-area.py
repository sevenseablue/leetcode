# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-12 上午7:14'
"""

from itertools import combinations
import math
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def count_triangle_area(p1, p2, p3):
            area = 0
            side = []
            side.append(math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)))
            side.append(math.sqrt(math.pow(p1[0] - p3[0], 2) + math.pow(p1[1] - p3[1], 2)))
            side.append(math.sqrt(math.pow(p3[0] - p2[0], 2) + math.pow(p3[1] - p2[1], 2)))
            if side[0] + side[1] <= side[2] or side[0] + side[2] <= side[1] or side[1] + side[2] <= side[0]:
                return area

            p = (side[0] + side[1] + side[2]) / 2    #  half circle
            area = math.sqrt(p * (p - side[0]) * (p - side[1]) * (p - side[2]))

            return area
        area = 0
        for p1, p2, p3 in combinations(points, 3):
            area = max(area,  count_triangle_area(p1, p2, p3))

        return area


solu = Solution()
points=[[0,0],[0,1],[1,0],[0,2],[2,0]]
print(solu.largestTriangleArea(points))




