# coding: utf8
"""
---------------------------------------------
    File Name: 6-zigzag-conversion
    Description: 
    Author: wangdawei
    date:   2018/4/23
---------------------------------------------
    Change Activity: 
                    2018/4/23
---------------------------------------------    
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        i, j, k = 0, 0, 0
        indexResult = []
        for k in range(len(s)):
            indexResult.append((i, j, k))
            if k % (2*(numRows - 1)) < numRows - 1:
                i += 1
            else:
                i -= 1
                j += 1
        indexResult = sorted(indexResult)
        return "".join([s[k] for _, _, k in indexResult])


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows>=len(s):
            return s
        i, j, k = 0, 0, 0
        indexResult = [''] * numRows
        for k in range(len(s)):
            indexResult[i] += s[k]
            if k % (2*(numRows - 1)) < numRows - 1:
                i += 1
            else:
                i -= 1
                j += 1
        return "".join(indexResult)

solu = Solution()
assert solu.convert("abc", 1) == "abc"
assert solu.convert("abc", 2) == "acb"
assert solu.convert("abc", 3) == "abc"
assert solu.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert solu.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"



