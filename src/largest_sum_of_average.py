# coding: utf8
"""
---------------------------------------------
    File Name: largest_sum_of_average
    Description: 
    Author: wangdawei
    date:   2018/4/11
---------------------------------------------
    Change Activity: 
                    2018/4/11
---------------------------------------------    
"""

from itertools import combinations
# print(len(list(combinations(list(range(100)), 50))))

import sys
class Solution:
    def largestSumOfAverages_dp_arrayall(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        alen = len(A)
        dp = [[[-sys.maxsize-1 for k in range(K+1)]for j in range(alen+1)] for i in range(alen)]
        cnt=0
        for k in range(1, K + 1):
            for i in range(0, alen):
                for j in range(i+1, alen+1):
                    # print(i,j,k)
                    if k == 1:
                        dp[i][j][k] = avg(A[i:j])
                    else:
                        for ji in range(i+k-1,j):
                            cnt += 1
                            v1 = dp[i][ji][k-1] + dp[ji][j][1]
                            if v1 > dp[i][j][k]:
                                dp[i][j][k] = v1

        print(cnt, "times")
        return dp[0][alen][K]

    def largestSumOfAverages_dp_3(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        alen = len(A)
        dp = [[-sys.maxsize-1 for j in range(alen+1)] for i in range(alen)]
        dp1 = [[-sys.maxsize-1 for j in range(alen + 1)] for i in range(alen)]
        cnt=0

        for i in range(0, alen):
            for j in reversed(range(i+1, alen+1)):
                dp1[i][j] = avg(A[i:j])
                pass

        if K == 1:
            return dp1[0][alen]

        for i in range(0, alen):
            for j in reversed(range(i+1, alen+1)):
                for ji in range(i + 1, j):
                    cnt += 1
                    v1 = dp1[i][ji] + dp1[ji][j]
                    if v1 > dp[i][j]:
                        dp[i][j] = v1

        for k in range(3, K + 1):
            for i in range(0, alen):
                for j in reversed(range(i+1, alen+1)):
                    for ji in range(i+k-1,j):
                        cnt += 1
                        v1 = dp[i][ji] + dp1[ji][j]
                        if v1 > dp[i][j]:
                            dp[i][j] = v1
                        pass

        print(cnt, "times")
        return dp[0][alen]


    def largestSumOfAverages_dp_2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        alen = len(A)
        dp = [[-float("inf") for j in range(alen+1)] for i in range(alen)]
        dp1 = [[-float("inf") for j in range(alen + 1)] for i in range(alen)]
        cnt=0
        for k in range(1, K + 1):
            for i in range(0, alen):
                for j in reversed(range(i+1, alen+1)):
                    # print(i,j,k)
                    if k == 1:
                        dp1[i][j] = avg(A[i:j])
                    else:
                        for ji in range(i+k-1,j):
                            cnt += 1
                            v1 = (dp[i][ji] + dp1[ji][j]) if k>2 else (dp1[i][ji] + dp1[ji][j])
                            if v1 > dp[i][j]:
                                dp[i][j] = v1
        return dp[0][alen]

    def largestSumOfAverages_dp_maxele(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        if K == 1:
            return avg(A)
        elif K == 2:
            return self.largestSumOfAverages_dp_3(A, 2)
        elif K == len(A):
            return sum(A)
        elif K == len(A)-1:
            minv = sys.maxsize
            for i in range(K):
                if sum(A[i:i+2])<minv:
                    minv = sum(A[i:i+2])
            return sum(A) - minv/2
        else:



            pass

def avg(l1):
    return sum(l1)/len(l1)
l1 = [1,2,5,3,4]
for i in range(1,5):
    print(avg(l1[:i])+avg(l1[i:]))

print(-sys.maxsize-1)

l1=[2192,348,3913,5028,5149,6264,248,1415,9081,1342,8624,2772,7666,2217,6123,5096,3203,98,3321,8733,7925,8869,9645,1686,2691,6267,4150,5184,401,6218,6682,5113,9758,4380,4366,4213,4226,4047,6748,4827,7158,666,3301,9753,5737,1780,2717,2180,7290,1145,3602,3569,7603,8084,64,7002,1722,9649,23,9368,3658,5002,1699,4578,7564,34,5875,3250,3803,4196,3921,7700,9682,5407,3476,595,2313,6780,3474,8304,3017,9449,2268,9525,9711,2135,5330,6653,7493,135,4153,3696,2003,3102,7982,8147,7397,2153,9405,4321]
print(len(l1))
K=99
import time
t1 = time.time()
solu = Solution()
print(solu.largestSumOfAverages_dp_arrayall(l1, K))
print(time.time()-t1)
t1 = time.time()
print(solu.largestSumOfAverages_dp_2(l1, K))
print(time.time()-t1)
t1 = time.time()
print(solu.largestSumOfAverages_dp_3(l1, K))
print(time.time()-t1)
t1 = time.time()
print(solu.largestSumOfAverages_dp_maxele(l1, K))
print(time.time()-t1)