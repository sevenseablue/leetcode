
import collections
class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        setA = set(A)
        for i in range(1, len(A)):
            for j in range(0, i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in setA:
                    dp[A[i], A[j]] = dp.get((A[j], A[i]-A[j]), 2) + 1
                    # print(A[i], A[j], dp[A[i], A[j]])

        return max(dp.values() or [0])

solu = Solution()
for A in [[1,3,7,11,12,14,18], [1,2,3,4,5,6,7,8]]:
    print(solu.lenLongestFibSubseq(A))