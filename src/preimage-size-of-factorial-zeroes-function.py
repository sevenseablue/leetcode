# -*- coding: utf-8 -*-
"""
__author__ = 'wangdawei'
__time__ = '18-4-12 上午8:07'
"""

import math
class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        five_ele = []
        for i in range(20):
            five_ele.append((i, int(math.pow(5, i))))
        five_ele=list(reversed(five_ele))


        ind = 1
        cnt = 0
        # for i, e in enumerate(five_ele):
        #     print(i, e)
        # return
        while True:
            print(cnt)
            if cnt == K:
                return 5
            if cnt > K:
                return 0
            num = ind*5
            for i, e in five_ele:
                # print(num, e, num%e)
                if e<=num and (num % e) == 0:
                    cnt += i
                    break
            ind += 1
            # break
print(10%10)
solu = Solution()
for i in range(200):
    print(i, solu.preimageSizeFZF(i))
i=1000000000
print(i, solu.preimageSizeFZF(i))
