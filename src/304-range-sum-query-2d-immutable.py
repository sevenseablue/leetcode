
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0]) if m != 0 else 0
        self.dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    self.dp[i][j] = self.matrix[i][j]
                else:
                    self.dp[i][j] = self.dp[i][j-1] + self.matrix[i][j]
        # print(self.dp)
        for i in range(1, m):
            for j in range(n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j]

        # print(self.dp)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        # print(self.dp[row2][col2] )
        # print(self.dp[row1 - 1][col2] if row1 > 0 else 0 )
        # print(self.dp[row2][col1 - 1] if col1 > 0 else 0 )
        # print(self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)
        return (self.dp[row2][col2] - (self.dp[row1-1][col2] if row1 > 0 else 0) - (self.dp[row2][col1-1] if col1> 0 else 0) + (self.dp[row1-1][col1-1] if row1>0 and col1>0 else 0))






# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
matrix = [[]]
obj = NumMatrix(matrix)
print(obj.sumRegion(0, 0, 0, 0))
exit()
for params in [[2,1,4,3], [1,1,2,2], [1,2,2,4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 3, 0]]:

    print("#" * 50)
    param_1 = obj.sumRegion(*params)

    print (param_1)