class Solution:
    # n**2
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -2**31-1
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum > maxSum:
                    maxSum = curSum

        return maxSum

    # n
    def maxSubArray(self, nums):
        maxSum = -2**31-1
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum>maxSum:
                maxSum = curSum
            if curSum<=0:
                curSum = 0

        return maxSum


    # n*logn, dp
    def maxSubArray(self, nums):

        def borderMax(nums, i1, i2):
            curSum = 0
            maxSum = -2**31-1
            for i in range(i1, i2, -1 if i1>i2 else 1):
                curSum += nums[i]
                if curSum > maxSum:
                    maxSum = curSum
            return maxSum

        def recur(nums, left, right):
            if left==right:
                return nums[left]
            if left+1 == right:
                return max(nums[left], nums[right], nums[left]+nums[right])

            mid = int((left + right) / 2)
            lSum = borderMax(nums, mid, left-1)
            rSum =  borderMax(nums, mid+1, right + 1)

            leftSum = recur(nums, left, mid)
            rightSum = recur(nums, mid+1, right)

            return max(leftSum, rightSum, lSum+rSum)
        # print("dp")
        return recur(nums, 0, len(nums)-1)

    # n, dp
    def maxSubArray(self, nums):
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0 or dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]

        return max(dp)

solu = Solution()
for nums in [[-2, -3, -1], [-2,1,-3,4,-1,2,1,-5,4]]:
    print(solu.maxSubArray(nums))



