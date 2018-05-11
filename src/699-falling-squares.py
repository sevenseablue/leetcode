
import bisect
class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        left, right, lr, height = [], [], [], []
        maxHeight = 0
        for x, y in positions:
            print(left, right, x, y)
            i = bisect.bisect_right(right, x)  # left most seg index
            j = bisect.bisect_left(left, x+y)  # right most seg index
            if len(left) == 0:
                left[i] = x
                right[i] = x+y
                height[i] = y
            else:
                ind = i
                if left[i]<x:
                    right[i] = x
                    ind = i+1
                else:
                    left.pop(i)
                    right.pop(i)
                    height.pop(i)
                    pass
                h = max(height[i:j + 1])+y
                left.insert(ind, x)
                right.insert(ind, x+y)
                height.insert(ind, +y)
                if right[j]>x+y:
                    left.insert(ind+1, left[j])
                    right.insert(ind+1, right[j])
                    height.insert(ind+1, height[j])


            for k in range(i, j+1):
                pass

            print(i, j)
            # if i == 0:
            #     if len(nums) == 0 or x+y<= nums[i+1]:
            #         nums[i] = x
            #         sidelen[i] = (x, 0, x+y, y)
            #         if y > maxHeight:
            #             maxHeight = y
            #     else:

solu = Solution()
positions = [[1, 4], [2, 1]]
solu.fallingSquares(positions)



