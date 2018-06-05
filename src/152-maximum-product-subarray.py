
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -2*31
        curProd = 1
        maxNega = 0
        for i in range(len(nums)):
            curProd *= nums[i]
            res = max(res, curProd)
            if curProd<0:
                if not maxNega:
                    maxNega = curProd
                else:
                    res = max(res, curProd // maxNega)
            if curProd == 0:
                curProd = 1
                maxNega = 0
        return res

solu = Solution()

for nums in [[2,3,-2,4], [-2,0,-1], [3,-1,4]]:
    print(solu.maxProduct(nums))