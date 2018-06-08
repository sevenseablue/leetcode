class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        minprice = 2**31
        for i in range(len(prices)):
            minprice = min(prices[i], minprice)
            if prices[i] - minprice > res:
                res = prices[i] - minprice

        return res

solu = Solution()
for prices in [[7,1,5,3,6,4],  [7,6,4,3,1], [], [1], [1, 2], [2, 1]]:
    print(solu.maxProfit(prices))