class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = x+1e-3
        while t - x/t > 1e-3:
            t = (t + x/t) / 2
            if int(t) == int(x/t):
                break
        intt, intxt = int(t), int(x/t)
        if intt**2>x:
            return intxt
        else:
            return intt

solu = Solution()
for i in [0, 1, 2, 3, 10, 100, 1000, 10000, 99999999999999999999, 1000000000000, 1000000000001]:
    print("#"*50, i)
    print(solu.mySqrt(i))

