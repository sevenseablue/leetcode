class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        go = ((-1, 0), (0, -1), (1, 0), (0, 1))
        mark = [[False]*n for _ in range(m)]
        def dfs(x, y):
            mark[x][y] = True
            if grid[x][y] == "0":
                return
            for dx, dy in go:
                newx, newy = dx + x, dy + y
                if 0<=newx<m and 0<=newy<n and not mark[newx][newy] and grid[newx][newy] != "0":
                    dfs(newx, newy)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if not mark[i][j]:
                    if grid[i][j] != "0":
                        cnt += 1
                    dfs(i, j)
        return cnt

solu = Solution()
grid=[
[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]
]
grid=[
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]
]
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print(solu.numIslands(grid))
