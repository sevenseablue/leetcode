class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minind = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= minind:
                minind = i

        if minind == 0:
            return True
        else:
            return False

solu = Solution()
for nums in [[2,3,1,1,4],[0],
             [3,2,1,0,4]]:
    print(solu.canJump(nums))
