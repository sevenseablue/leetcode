# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-14 上午9:24'
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        max_shuiping = [max(grid[i]) for i in range(n)]
        max_chuizhi = [-1 for i in range(n)]
        for i in range(n):
            for j in range(n):
                max_chuizhi[i] = max(max_chuizhi[i], grid[j][i])
        # print(max_chuizhi, max_shuiping)
        cnt = 0
        for i in range(n):
            for j in range(n):
                cnt += min(max_shuiping[i], max_chuizhi[j]) - grid[i][j]

        return cnt



solu = Solution()
grid = [ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
print(solu.maxIncreaseKeepingSkyline(grid))





