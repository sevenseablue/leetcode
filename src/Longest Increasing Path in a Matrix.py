# coding: utf8
"""
---------------------------------------------
    File Name: Longest Increasing Path in a Matrix
    Description: 
    Author: wangdawei
    date:   2018/2/8
---------------------------------------------
    Change Activity: 
                    2018/2/8
---------------------------------------------    
"""


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ml = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # print(ml)
        e_l = [(matrix[i][j], i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
        e_l_sort = sorted(e_l, key=lambda x: x[0], reverse=True)
        result = 0
        for e, i, j in e_l_sort:
            tmp = []
            if i - 1 >= 0 and matrix[i - 1][j] > e:
                tmp.append(ml[i - 1][j])
            if i + 1 < len(matrix) and matrix[i + 1][j] > e:
                tmp.append(ml[i + 1][j])
            if j - 1 >= 0 and matrix[i][j - 1] > e:
                tmp.append(ml[i][j - 1])
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > e:
                tmp.append(ml[i][j + 1])
            if tmp == []:
                ml[i][j] = 1
            else:
                ml[i][j] = max(tmp) + 1
            if ml[i][j] > result:
                result = ml[i][j]
        return result


# DFS + Memorization solution.
class Solution_rec(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]

            max_depth = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths))
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]

        res = 0
        max_lengths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, longestpath(matrix, i, j, max_lengths))

        return res

import time

solu = Solution()
solu2 = Solution_rec()
nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
# tmp = list(range(10000))
nums = []
rank = 2000
for i in range(rank):
    ind = i * rank
    tmp = list(range(ind, ind + rank))
    if i%2==1:
        tmp.reverse()
    nums.append(tmp)
# import random
# for i in range(rank):
#     tmp = []
#     for j in range(rank):
#         tmp.append(random.randint(0, rank*rank))
#     nums.append(tmp)
t1 = time.time()
r1 = solu.longestIncreasingPath(nums)
print(time.time() - t1)
t1 = time.time()
r2 = solu2.longestIncreasingPath(nums)
print(time.time() - t1)
t1 = time.time()
print(r1, r2)