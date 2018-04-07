# coding: utf8
"""
---------------------------------------------
    File Name: Cherry Pickup
    Description: 
    Author: wangdawei
    date:   2018/3/14
---------------------------------------------
    Change Activity: 
                    2018/3/14
---------------------------------------------    
"""

import copy


class Solution2:
    def pickupOnce(self, grid):
        width = len(grid[0])
        height = len(grid)
        n = copy.deepcopy(grid)
        for i in range(1, width):
            if n[0][i - 1] == -1 or grid[0][i] == -1:
                n[0][i] = -1
            else:
                n[0][i] = n[0][i - 1] + grid[0][i]
        for i in range(1, height):
            if n[i - 1][0] == -1 or grid[i][0] == -1:
                n[i][0] = -1
            else:
                n[i][0] = n[i - 1][0] + grid[i][0]

        for i in range(1, height):
            for j in range(1, width):
                if (n[i - 1][j] == -1 and n[i][j - 1] == -1) or grid[i][j] == -1:
                    n[i][j] = -1
                elif n[i - 1][j] == -1:
                    n[i][j] = n[i][j - 1] + grid[i][j]
                elif n[i][j - 1] == -1:
                    n[i][j] = n[i - 1][j] + grid[i][j]
                else:
                    n[i][j] = max(n[i - 1][j], n[i][j - 1]) + grid[i][j]
        return n

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        # print(grid)
        width = len(grid[0])
        height = len(grid)
        n = self.pickupOnce(grid)
        if n[height - 1][width - 1] == -1:
            return 0
        self.travel(n, grid)
        # print(grid)
        nb = self.pickupOnce(grid)
        return n[height - 1][width - 1] + nb[height - 1][width - 1]

    def travel(self, n, grid):
        width = len(grid[0])
        height = len(grid)
        i, j = height - 1, width - 1
        while not (i == 0 and j == 0):
            grid[i][j] = 0
            if i - 1 >= 0 and j - 1 >= 0:
                if n[i - 1][j] >= n[i][j - 1]:
                    i = i - 1
                else:
                    j = j - 1
            elif i - 1 < 0:
                j = j - 1
            else:  # j-1<0
                i = i - 1
        grid[0][0] = 0

        pass


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp holds the max # of cherries two k-length paths can pickup.
        # The two k-length paths arrive at (i, k - i) and (j, k - j),
        # respectively.
        n = len(grid)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        max_len = 2 * (n - 1)
        directions = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        for k in range(1, max_len + 1):
            for i in reversed(range(max(0, k - n + 1), min(k + 1, n))):  # 0 <= i < n, 0 <= k-i < n
                for j in reversed(range(i, min(k + 1, n))):  # i <= j < n, 0 <= k-j < n
                    if grid[i][k - i] == -1 or grid[j][k - j] == -1:
                        dp[i][j] = -1
                        continue
                    cnt = grid[i][k - i]
                    if i != j:
                        cnt += grid[j][k - j]
                    max_cnt = -1
                    for direction in directions:
                        ii, jj = i + direction[0], j + direction[1]
                        if ii >= 0 and jj >= 0 and dp[ii][jj] >= 0:
                            max_cnt = max(max_cnt, dp[ii][jj] + cnt)
                    dp[i][j] = max_cnt
        return max(dp[n - 1][n - 1], 0)


envs = [
    [
        [0, 1, -1],
        [1, 0, -1],
        [1, 1, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ],
    [
        [0, 1, -1],
        [1, 0, -1],
        [1, -1, 1]
    ],
    [
        [1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],

    ],
]
solu = Solution()
for env in envs:
    print(solu.cherryPickup(env))
