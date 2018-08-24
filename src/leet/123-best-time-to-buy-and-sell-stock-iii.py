class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = []
        last_price = 2 ** 31
        min_price = last_price
        for price in prices:
            if price <= last_price:
                res.append(last_price - min_price)
                min_price = price

            last_price = price
        res.append(last_price - min_price)
        return sum(sorted(res, reverse=True)[:2])

solu = Solution()
for prices in [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 3, 1], [], [1], [1, 2], [1,2,4,2,5,7,2,4,9,0]]:
    # print(prices)
    print(solu.maxProfit(prices))

