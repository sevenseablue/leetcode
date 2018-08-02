class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        Asub = []
        for i in range(len(A)-1):
            Asub.append(A[i+1] - A[i])

        lastSub = Asub[0]
        sameSeg = [1]
        for i in range(1, len(A) - 1):
            if Asub[i] == lastSub:
                sameSeg[-1] += 1
            else:
                lastSub = Asub[i]
                sameSeg.append(1)

        res = 0
        for i in range(len(sameSeg)):
            if sameSeg[i] > 1:
                res += (sameSeg[i] - 1)*(sameSeg[i]) / 2

        return res

solu = Solution()
A = [1, 2, 3, 4]
for i in range(1, 6):
    A = list(range(i))
    print(solu.numberOfArithmeticSlices(A))
