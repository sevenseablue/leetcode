# coding: utf8
"""
---------------------------------------------
    File Name: 524-longest-word-in-dictionary-through-deleting
    Description: 
    Author: wangdawei
    date:   2018/4/18
---------------------------------------------
    Change Activity: 
                    2018/4/18
---------------------------------------------    
"""


class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        keys=list(sorted(d, key=lambda x:(-len(x), x)))
        # print(keys)
        n_s = len(s)
        for k in keys:
            n_k = len(k)
            if n_s < n_k:
                continue
            i,j=0, 0
            while i<n_s and j<n_k:
                if s[i] != k[j]:
                    i += 1
                    continue
                else:
                    i += 1
                    j += 1
            if j==n_k:
                return k
        return ""
# print(ord("a"))
solu = Solution()
s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print(solu.findLongestWord(s, d))
s = "abpcplea"
d = ["a","b","c"]
print(solu.findLongestWord(s, d))