

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)

        return heap[0]


solu = Solution()
nums = [3,2,1,5,6,4]
k = 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(solu.findKthLargest(nums, k))