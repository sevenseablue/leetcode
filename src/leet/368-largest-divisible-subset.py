
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        dp = [1] * len(nums)
        divi = {}
        for i in range(len(nums)):
            divi[i] = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        divi[i] = divi[j]+[nums[i]]
        res = []
        for i in range(len(nums)):
            if dp[i] > len(res):
                res = divi[i]

        return res

solu = Solution()

for nums in [[], [1], [1,2,3], [1, 2, 4, 8], [2, 3, 9, 18]]:
    print(solu.largestDivisibleSubset(nums))