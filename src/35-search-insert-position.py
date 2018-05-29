class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r = 0, len(nums)-1
        ln = len(nums)

        while l<=r:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            elif 0<=mid+1<ln and  nums[mid]<target<nums[mid+1]:
                return mid+1
            else:
                l = mid + 1
        return l

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r = 0, len(nums)-1

        while l<=r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return l


nums = [1,3,5,6]
solu = Solution()
for i in range(0, 8):
    print(i, solu.searchInsert(nums,i))
