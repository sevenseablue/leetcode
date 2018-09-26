# coding: utf8
"""
---------------------------------------------
    File Name: Trapping Rain Water
    Description: 
    Author: wangdawei
    date:   2018/1/12
---------------------------------------------
    Change Activity: 
                    2018/1/12
---------------------------------------------    
"""





class Solution(object):


    def cal_water(self, height, last_trap_ind, ind):
        h = min(height[last_trap_ind], height[ind])
        result = 0
        for i in range(last_trap_ind+1, ind):
            result += h - height[i]
        return result


    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        la = len(height)
        if la < 3:
            return 0
        max_ind = [-1] * 2
        max_v = -1
        for i in range(la):
            if height[i] > max_v:
                max_v = height[i]
                max_ind[0], max_ind[1] = i, i
            elif height[i] == max_v:
                max_ind[1] = i

        trap_flag = [False] * la
        trap_flag[max_ind[0]] = True
        trap_flag[max_ind[1]] = True
        max_v_l = -1
        for i in range(max_ind[0]):
            if height[i] >= max_v_l:
                max_v_l = height[i]
                trap_flag[i] = True
        max_v_l = -1
        for i in range(la-1, max_ind[1], -1):
            if height[i] >= max_v_l:
                max_v_l = height[i]
                trap_flag[i] = True

        if trap_flag[0] is False:
            raise Exception("0 false")

        last_trap_ind = 0
        water = 0
        for i in range(1, la):
            if trap_flag[i]:
                water_tmp = self.cal_water(height, last_trap_ind, i)
                water += water_tmp
                last_trap_ind=i

        return water
h
def main():
    solu = Solution()
    # print(solu.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    assert solu.trap([0,1,0,2,1,0,1,3,2,1,2,1])== 6
    assert solu.trap([]) == 0
    assert solu.trap([1]) == 0
    assert solu.trap([1,2]) == 0
    assert solu.trap([1, 2, 3]) == 0
    assert solu.trap([2, 1, 3]) == 1

if __name__ == "__main__":
    main()