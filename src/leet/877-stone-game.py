

class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = piles.copy()
        dp2 = dp.copy()
        dsum = [[0]]
        for i in range(len(piles)):

        for i in range(2, len(piles)+1):
            for j in range(0, len(piles)-i+1):
                dp[j] = max()
