
class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        lastflag = 0
        flag = 0
        result = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if nums[i] - nums[i-1] > 0:
                flag = 1
            else:
                flag = -1
            if not lastflag or lastflag + flag == 0:
                result += 1

            lastflag=flag

        return result

solu = Solution()
for nums in [[1,17,5,10,13,15,10,5,16,8],
             [],
             [1],
             [1,2],
             [1,2,1],
             [1,2,3,3,3,4,1],
             [1,7,4,9,2,5],
             [1,2,3,4,5,6,7,8,9]]:
    print(solu.wiggleMaxLength(nums))
