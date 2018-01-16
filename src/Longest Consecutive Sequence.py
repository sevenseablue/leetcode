# coding: utf8
"""
---------------------------------------------
    File Name: Longest Consecutive Sequence
    Description: 
    Author: wangdawei
    date:   2018/1/16
---------------------------------------------
    Change Activity: 
                    2018/1/16
---------------------------------------------    
"""


class Solution:
    def longestConsecutive_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        maxl = 0
        for n in nums:
            if n not in d:
                l = n if n - 1 not in d else d[n-1][0]
                r = n if n + 1 not in d else d[n+1][1]
                d[l] = (l, r)
                d[r] = (l, r)
                d[n] = (l, r)
                tmp_l = r - l + 1
                if tmp_l > maxl:
                    maxl = tmp_l

        return maxl


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxl = 0
        for n in nums:
            if n - 1 not in nums:
                y = n + 1
                while y in nums:
                    y += 1
                maxl = max(maxl, y - n)

        return maxl




def main():
    solu = Solution()
    print(solu.longestConsecutive([100, 4, 200, 1, 3, 2]))

if __name__ == "__main__":
    main()

