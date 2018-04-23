# coding: utf8
"""
---------------------------------------------
    File Name: 1-two-sum
    Description: 
    Author: wangdawei
    date:   2018/4/20
---------------------------------------------
    Change Activity: 
                    2018/4/20
---------------------------------------------    
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numCount = {}
        for i in range(len(nums)):
            cInd = numCount.setdefault(nums[i], [0, []])
            cInd[0] += 1
            cInd[1].append(i)
            # numCount[nums[i]] = cInd
        print(numCount)
        for i in range(len(nums)):
            subtract = target - nums[i]
            if subtract in numCount:
                if subtract != nums[i]:
                    return [i, numCount[subtract][1][0]]
                else:
                    cInd = numCount.get(subtract)
                    if cInd[0] == 2:
                        return [i, cInd[1][1]]
        return []


solu = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solu.twoSum(nums, target))




