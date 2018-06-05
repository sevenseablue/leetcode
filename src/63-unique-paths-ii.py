class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (n + 1)
        dp[n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + dp[j+1]
        return dp[0]


solu = Solution()
obstacleGrid = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
obstacleGrid=[[0,0]]
print(solu.uniquePathsWithObstacles(obstacleGrid))