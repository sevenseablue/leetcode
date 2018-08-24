class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [2**31] * (n + 1)
        dp[1] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = min(dp[j-1], dp[j]) + grid[i-1][j-1]
        return dp[-1]

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
# grid = [[1, 2], [1, 1]]
grid = [[1,2,5],[3,2,1]]
solu = Solution()
print(solu.minPathSum(grid))
