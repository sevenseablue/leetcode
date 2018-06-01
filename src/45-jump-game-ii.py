

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        times = 0
        seg = [0, 0]
        while True:
            times += 1
            s,e=seg[1]+1, seg[1]
            for i in range(seg[0], seg[1]+1):
                if nums[i]+i>e:
                    e = nums[i]+i

            if s>e or e>=len(nums)-1:
                break
            seg = (s, e)


        return times if e >= len(nums) -1 else -1

solu = Solution()

for nums in [[2,3,1,1,4], [0], [1,1,1,1], [1,0,0,4]]:
    print(solu.jump(nums))