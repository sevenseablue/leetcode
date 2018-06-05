class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                    continue
                if word1[i-1:i] == word2[j-1:j]:
                    dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

        # print(dp)
        return dp[l1][l2]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dpPre = [0]*(l2+1)
        dpCur = [0]*(l2+1)
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0 or j == 0:
                    dpCur[j] = max(i, j)
                    continue
                if word1[i-1:i] == word2[j-1:j]:
                    dpCur[j] = dpPre[j-1]
                else: dpCur[j] = min(dpPre[j], dpCur[j-1], dpPre[j-1])+1

            dpPre = dpCur
            dpCur = [0]*(l2+1)

        # print(dp)
        return dpPre[l2]


solu = Solution()
word1 = "horse"
word2 = "ros"
# word1 = "intention"
# word2 = "execution"
# word1 = ""
# word2 = "a"
word1 = "a"
word2 = "ab"
print(solu.minDistance(word1, word2))