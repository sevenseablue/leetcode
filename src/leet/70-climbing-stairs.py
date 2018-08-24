
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache={0:0, 1:1, 2:2}
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def dfs(i):
            if i <= 2:
                cache[i] = i
                return i
            if i in cache:
                return cache[i]
            cache[i] = dfs(i - 1) + dfs(i - 2)
            return cache[i]

        return dfs(n)

solu = Solution()
print(solu.climbStairs(35))
for i in range(10):
    print(solu.climbStairs(i))