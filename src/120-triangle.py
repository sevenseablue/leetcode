class Solution:

    def minimumTotal(self, triangle):

        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        def minmy(dpup, j, i):
            if j - 1 < 0:
                return dpup[j]
            if j > i:
                return dpup[j - 1]
            return min(dpup[j - 1], dpup[j])

        lt = len(triangle)
        dp1 = [2**31 for _ in range(lt)]
        dp2 = [2 ** 31 for _ in range(lt)]
        dp2[0] = triangle[0][0]
        dpdown = dp2
        for i in range(1, lt):
            if i % 2 == 0:
                dpup = dp1
                dpdown = dp2
            else:
                dpup = dp2
                dpdown = dp1

            for j in range(i+1):
                dpdown[j] = minmy(dpup, j, i-1)+triangle[i][j]

        return min(dpdown)



triangle =[
     [2],
    [3,4],
   [6,5,1],
  [4,1,8,1]
]
solu = Solution()
print(solu.minimumTotal(triangle))

