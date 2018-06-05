class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob1(nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[len(nums) - 1]

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(rob1(nums[:-1]), rob1(nums[1:]))

solu = Solution()
for nums in [[2,3,2],
             [1,2,3,1],
             [],
             [1],
             [2, 3]]:
    print(solu.rob(nums))
