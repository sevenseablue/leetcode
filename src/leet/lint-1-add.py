# coding: utf8
"""
---------------------------------------------
    File Name: lint-1-add
    Description: 
    Author: wangdawei
    date:   2018/4/24
---------------------------------------------
    Change Activity: 
                    2018/4/24
---------------------------------------------    
"""

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def add(self, a, b):
        {("0", )}
    def aplusb(self, a, b):
        # write your code here
        sa = str(a)
        sb = str(b)
        sa = sa[::-1]
        sb = sb[::-1]
        if len(sa)>=len(sb):
            sb += "0"*(len(sa) - len(sb))
        else:
            sa += "0" * (len(sb)-len(sa))
        cumm = 0
        res = []
        for ae, be in zip(sa, sb):
            print(ae, be)
            res.append(int(ae))



solu = Solution()
print(solu.aplusb(1123, 999))

