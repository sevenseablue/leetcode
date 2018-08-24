#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[j] = dp[j+1] + dp[j]

        return dp[0]

solu = Solution()
m = 2
n = 2
# m = 7
# n = 3
print(solu.uniquePaths(m, n))
