
import copy
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        matrix = [ [0 for i in range(n)] for j in range(n)]

        def update(matrix, ind, i):
            for j in range(ind+1, n):
                matrix[j][i] += -1
                right = i+j-ind
                left = i-j+ind
                if right >=0 and right < n:
                    matrix[j][right] += -1
                if left >= 0 and left < n:
                    matrix[j][left] += -1
        def revert(matrix, ind, i):
            for j in range(ind+1, n):
                matrix[j][i] += 1
                right = i+j-ind
                left = i-j+ind
                if right >=0 and right < n:
                    matrix[j][right] += 1
                if left >= 0 and left < n:
                    matrix[j][left] += 1
        def dfs(ind):
            if ind == n:
                result.append(copy.deepcopy(matrix))
                return
            for i in range(n):
                if matrix[ind][i] == 0:
                    matrix[ind][i] = 1
                    update(matrix, ind, i)
                    dfs(ind + 1)
                    matrix[ind][i] = 0
                    revert(matrix, ind, i)

        dfs(0)
        res = []
        for m in result:
            tmp = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if m[i][j] == 1:
                        row = row +"Q"
                    else:
                        row += "."
                tmp.append(row)
            res.append(tmp)


        return res

solu = Solution()
for i in range(1, 11):
    result = solu.solveNQueens(i)
    print(result)
    print("result, ", len(result))

