class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xs = str(x)
        return xs == xs[::-1]


solu = Solution()
for x in [121, -121]:
    print(solu.isPalindrome(x))
