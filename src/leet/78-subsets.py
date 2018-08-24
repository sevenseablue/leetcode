
class Solution:
    def __init__(self):
        self.result = []
    def sub(self, i, nums, item):
        if i >= len(nums):
            self.result.append(item.copy())
            return
        item.append(nums[i])
        self.sub(i + 1, nums, item)
        item.pop()
        self.sub(i + 1, nums, item)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        item = []
        def sub(i):
            if i >= len(nums):
                result.append(item.copy())
                return
            item.append(nums[i])
            sub(i + 1)
            item.pop()
            sub(i + 1)
        sub(0)
        return result

solu = Solution()
result = solu.subsets([1,2,3])
print(result)

