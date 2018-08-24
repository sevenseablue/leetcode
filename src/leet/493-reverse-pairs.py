# coding: utf8
"""
---------------------------------------------
    File Name: 493-reverse-pairs
    Description: 
    Author: wangdawei
    date:   2018/4/19
---------------------------------------------
    Change Activity: 
                    2018/4/19
---------------------------------------------    
"""
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

def mergeSortNum(alist):
    # print("Splitting ",alist)
    num = 0
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        num += mergeSortNum(lefthalf)
        num += mergeSortNum(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

        i = 0
        j = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i]/2 > righthalf[j]:
                num += len(lefthalf)-i
                j = j + 1
            else:
                i = i + 1

    # print("Merging ",alist)
    return num


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print("Splitting ",alist)
        alist = nums
        num = 0
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            num += self.reversePairs(lefthalf)
            num += self.reversePairs(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j + 1
                k = k + 1

            i = 0
            j = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] / 2 > righthalf[j]:
                    num += len(lefthalf) - i
                    j = j + 1
                else:
                    i = i + 1
            # prev_total = 0
            # mid = 0
            # for i in range(0, len(lefthalf)):
            #     target = lefthalf[i] - 1 >> 1
            #     idx = bisect.bisect_right(righthalf, target, mid, len(righthalf))
            #     prev_total += idx
            #     mid = idx
            #     num += prev_total

        # print("Merging ",alist)
        return num


import bisect

class Solution2(object):
    def reversePairs(self, nums):
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, l, r):
        mid = l + r >> 1
        if mid == l: return 0
        total = self.helper(nums, l, mid) + self.helper(nums, mid, r)
        prev_total = 0
        for i in range(l, mid):
            target = nums[i] - 1 >> 1
            idx = bisect.bisect_right(nums, target, mid, r)
            prev_total += idx - mid
            mid = idx
            total += prev_total
        nums[l: r] = sorted(nums[l: r])
        return total

solu = Solution()
solu2 = Solution2()
# alist = [54,26,93,17,77,31,44,55,20]
import time
t0 = time.time()
alist = list(range(50000))
print(solu.reversePairs(alist))
print(alist)
print(time.time() - t0)


