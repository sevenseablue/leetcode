# coding: utf8
"""
---------------------------------------------
    File Name: First Missing Positive
    Description: 
    Author: wangdawei
    date:   2018/1/12
---------------------------------------------
    Change Activity: 
                    2018/1/12
---------------------------------------------    
"""


class Solution(object):
    def posi(self, v):
        return v - 1

    def place_num(self, nums, ind):
        inds, inde = 0, len(nums)
        now_p = ind
        num = nums[now_p]
        to_p = self.posi(num)
        if inds <= to_p < inde:
            if to_p != now_p:
                if nums[to_p] != num:
                    swap = nums[to_p]
                    nums[to_p] = num
                    nums[now_p] = swap
                    self.place_num(nums, ind)

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print("#"*50)
        for i in range(len(nums)):
            self.place_num(nums, i)
        # print(nums)
        for i in range(len(nums)):
            if i != self.posi(nums[i]):
                return i + 1
        return len(nums) + 1

def main():
    solu = Solution()
    assert solu.firstMissingPositive([]) == 1
    assert solu.firstMissingPositive([3]) == 1
    assert solu.firstMissingPositive([1, 2, 0]) == 3
    print("result", solu.firstMissingPositive([3, 4, -1, 1]))
    assert solu.firstMissingPositive([3, 4, -1, 1]) == 2
    assert solu.firstMissingPositive([0, 0, 0]) == 1
    assert solu.firstMissingPositive([1, 2, 3]) == 4
    assert solu.firstMissingPositive([1, 1, 1]) == 2

if __name__ == "__main__":
    main()