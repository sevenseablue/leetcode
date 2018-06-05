#!/home/wangdawei/anaconda2/envs/py3/bin/python 
# -*- coding: utf-8 -*-  
""" 
 @desc: 
 @author: wangdawei 
 @contact: 178129482@qq.com  
"""


class Solution:
    def common_seg(self, seg1, seg2):
        if seg1 and seg2 and seg2[0] <= seg1[1]:
            return (seg2[0], min(seg1[1], seg2[1]))
        else:
            return None
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points)
        # print(points)
        result = 0
        common_seg = None
        for p in points:
            cseg = self.common_seg(common_seg, p)
            if cseg:
                common_seg = cseg
            else:
                common_seg = p
                result += 1

        return result



solu = Solution()
for points in [ [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]], [[10,16], [2,8], [1,6], [7,12]], [[1,2]], [[1,2], [2,3]], [[1,5], [3,4]], [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]]:
    print(solu.findMinArrowShots(points))
