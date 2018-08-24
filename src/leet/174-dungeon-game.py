class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dp = [2**31] * (len(dungeon[0]) + 1)
        dp[-2] = 1
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                dp[j] = max(1, min(dp[j+1], dp[j]) - dungeon[i][j])
            # print(dp)
        return dp[0]



dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
dungeon = [[1,-3,3],
           [0,-2,0],
           [-3,-3,-3]]
solu = Solution()
print(solu.calculateMinimumHP(dungeon))