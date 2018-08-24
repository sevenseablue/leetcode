

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        dp = [1] * ln
        maxl = 0
        for i in range(0, ln):
            for j in range(0, i):
                if nums[j] < nums[i] and dp[i]<dp[j]+1:
                    dp[i] = dp[j] + 1
            if maxl < dp[i]:
                maxl = dp[i]

        return maxl


import bisect
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        dp = []

        for i in range(0, ln):
            if not dp or dp[-1] < nums[i]:
                dp.append(nums[i])

            else:
                ind = bisect.bisect_left(dp, nums[i])
                dp[ind] = nums[i]

        return len(dp)





nums = [10,9,2,5,3,7,101,18]
nums = [-1, 2, 2, 2, 3, 0, 0, 0, 1, 2]
solu = Solution()
print(solu.lengthOfLIS(nums))


