class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp1 = None
        res = 0

        for i in range(1, min(m, n) + 1):
            dp2 = [[0] * (n - i + 1) for _ in range(m - i + 1)]
            for j in range(m - i + 1):
                for k in range(n - i + 1):
                    if i == 1 and matrix[j][k] == "1" or (
                            i > 1 and dp1[j][k] and dp1[j + 1][k] and dp1[j][k + 1] and dp1[j + 1][k + 1]):
                        dp2[j][k] = 1
                        res = i
            if res < i:
                break
            dp1 = dp2
        return res*res


solu = Solution()
matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0], ]
matrix = [["0"]]
matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
print(solu.maximalSquare(matrix))
