class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        t = num + 1e-3
        while t - num/t > 1e-3:
            t = (t+num/t)/2
            if int(t) == int(num/t):
                break
        intt, intp = int(t), int(num/t)
        print(intt)
        if intt*intt == num:
            return True
        else:
            return False


solu = Solution()
for i in [0, 1, 2, 3, 10, 100, 1000, 10000, 99999999999999999999, 1000000000000, 1000000000001]:
    print("#"*50, i)
    print(solu.isPerfectSquare(i))