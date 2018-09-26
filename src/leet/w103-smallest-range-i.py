class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        K = K if K >=0 else -K
        maxa, mina = -2**31, 2**31
        for i in range(len(A)):
            maxa = max(maxa, A[i])
            mina = min(mina, A[i])

        gap = maxa -mina
        if gap <= 2*K:
            return 0
        else:
            return gap - 2*K

