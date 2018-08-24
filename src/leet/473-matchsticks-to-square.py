
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nsum = sum(nums)
        leng = nsum//4
        if leng*4 != nsum:
            return False
        nums = sorted(nums, reverse=True)
        target = leng
        mark = [False] * len(nums)
        for k in range(4):
            sum1 = 0
            for i in range(len(nums)):
                if mark[i]:
                    continue
                sum1 += nums[i]
                mark[i] = True
                if sum1 == target:
                    break
                if sum1 > target:
                    mark[i] = False
                if sum1 < target:
                    continue




nums = [1,1,2,2,2]
solu = Solution()
print(solu.makesquare(nums))