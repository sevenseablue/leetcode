class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = {0:(0, True)}
        for c in coins:
            cache[c] = 1, True

        self.cacheHit = 0
        self.minChange = {}
        def cc(coins, amount):
            if amount in cache:
                self.cacheHit += 1
                return cache[amount]

            for c in coins:
                if amount >= c :
                    cache.get(amount - c)
                    num, Flag = cc(coins, amount - c)
                    if Flag:
                        minc, flag = cache.get(amount, (0, False))
                        if not flag or 1+num<minc:
                            cache[amount] = num+1, True
            if amount not in cache:
                cache[amount] = 0, False
            return cache[amount]

        num, flag = cc(sorted(coins, reverse=True), amount)
        print("cacheHit, ", self.cacheHit)
        if flag:
            return num
        else:
            return -1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c<=i:
                    dp[i] = min(dp[i], dp[i-c]+1)

        return -1 if dp[amount] > amount else dp[amount]


class Solution:
    result = -1

    def dp(self, coins, idx, remain, cnt, checked=False):
        if cnt >= self.result:
            return False

        if not checked:
            q = remain // coins[idx]
            if remain % coins[idx] == 0:
                self.result = min(self.result, cnt + q)
                return True
            elif cnt + q + 1 >= self.result:
                return False

        if idx > 0:
            if coins[idx] < remain:
                self.dp(coins, idx, remain - coins[idx], cnt + 1, True)
            self.dp(coins, idx - 1, remain, cnt)

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        N = len(coins)
        coins.sort()
        self.result = amount + 1

        self.dp(coins, N - 1, amount, 0)

        if self.result <= amount:
            return self.result
        else:
            return -1

import time
t1 = time.time()
solu = Solution()
coins = [1, 2, 5]
amount = 11
coins = [1]
amount = 0
coins = [19,28,176,112,30,260,491,128,70,137,253]
amout = 8539
coins = [70,177,394,428,427,437,176,145,83,370]
amount = 7582
print(solu.coinChange(coins, amount))
print(time.time()-t1)


