# coding: utf8
"""
---------------------------------------------
    File Name: 240-search-a-2d-matrix-ii
    Description: 
    Author: wangdawei
    date:   2018/4/18
---------------------------------------------
    Change Activity: 
                    2018/4/18
---------------------------------------------    
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = 0, 0
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            n = 0
        while 0<=i<m and 0<=j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                if j<n-1 and matrix[i][j+1]<=target:
                    j += 1
                else:
                    i += 1
            elif matrix[i][j] > target:
                j -= 1


        if 0<=i<m and 0<=j<n:
            return True
        else:
            return False

solu = Solution()
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
m = []
for i in range(0, 33):
    print(i, solu.searchMatrix(m, i))

