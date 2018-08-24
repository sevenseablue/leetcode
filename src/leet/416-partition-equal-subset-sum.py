

class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def find(nums, target, marked, ind):
            if ind== len(nums):
                if target == 0:
                    return True
                return False
            if target == 0:
                return True
            if target < 0:
                return False

            marked[ind] = 1
            target -= nums[ind]
            flag = find(nums, target, marked, ind+1)
            if flag is True:
                return True
            marked[ind] = 0
            target += nums[ind]
            flag = find(nums, target, marked, ind + 1)
            if flag is True:
                return True
            return False

        if sum(nums)%2==1:
            return False
        marked = [0 for _ in range(len(nums))]
        return find(nums, sum(nums)//2, marked, 0)

class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1 = sum(nums)
        if (sum1 & 1) == 1:
            return False
        sum1 /= 2
        dp = {0:True}

        for num in nums:
            for i in list(dp.keys()):
                dp[i+num] = True

        return True if sum1 in dp else False


solu = Solution()
for nums in [[1,2,3,5], [1,5,5,11]]:
    print(solu.canPartition(nums))

